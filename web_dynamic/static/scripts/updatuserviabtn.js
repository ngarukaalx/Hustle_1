//wait for the dom to load
const urlParams = new URLSearchParams(window.location.search);
let bizId = urlParams.get('bizData');
let businessId;
$.ajax({
    url: "http://127.0.0.1:5001/api/v1/bizna/" + bizId,
    method: "GET",
    headers: {
        'Content-Type': 'application/json'
    },
    success: function (data) {
        $.each(data, function(index, biz) {
            const section1 = $('<section>').addClass('details');
            const div1 = $('<div>').addClass('logo-biz');
            const image = $('<img>');
            const div2 = $('<div>').addClass('busines-name');
            const bizName = $('<h2>').text(biz.name);
            const p1 = $('<p>').text('County: ' + biz.county_name);
            const p2 = $('<p>').text('Town:' + biz.town_name);
            const p3 = $('<p>').text(biz.exact_location);
            // create a url for logo
            const logoUrl = "http://127.0.0.1:5001/api/v1/uploads/" + biz.logo;
            console.log(logoUrl);
        image.attr({
            src: logoUrl,
            alt: 'logo'
        });
        div1.append(image);
        div2.append(bizName);
        section1.append(div1, div2, p1, p2, p3);
        $('.busines-details').append(section1);
        // updta business description
        const h3 = $('<h3>').text('Dealers in: ' + biz.description);
        const br = $('<br>');
        $('.bs-desc').append(h3, br);
        return false;
    });
    // Fetch videos related to this business
    $.ajax({
            url: `http://127.0.0.1:5001/api/v1/businesses/${bizId}/videos`,
            method: "GET",
            headers: {
                    'Content-Type': 'application/json'
            },
            success: function (data) {
                    $.each(data, function(index, video) {
                            const sec2 = $('<section>').addClass('list-vid');
                            const vid = $('<video controls>');
                            const source = $('<source>');
                            // set attributes for the source element
                            const videourl = "http://127.0.0.1:5001/api/v1/uploads/" + video.url;
                            source.attr({
                                    src: videourl,
                                    type: 'video/mp4'
                            });
                            const div = $('<div>').addClass('desc');
                            const p = $('<p>').attr('id', 'desc');
                            vid.append(source);
                                  p.text(video.description);
                                  div.append(p);
                                  sec2.append(vid, div);
                                  $('.vids').append(sec2);

                          });
                  },
                  error: function(stats, error) {
                          console.error(stats, error);
                  }
          });
          $('#uploadForm').submit(function (event) {
          event.preventDefault(); //prevent traditional submission
          // create the form data for video file
          const videoInput = document.getElementById('videoFile');
          let videForm = new FormData();
          let file = videoInput.files[0];
          // Get the description
          const description = $('#description').val();
          if (file) {
              videForm.append('file', file);
              videForm.append('business_id', businessId);
              videForm.append('description', description);
          }
          $.ajax({
              url: "http://127.0.0.1:5001/api/v1/uploadvideo",
              method: "Post",
              processData: false,
              contentType: false,
              data: videForm,
              success: function (response) {
                  console.log(response);
              },
              error: function(stats, error) {
                  console.error(stats, error);
              }
          });
      });
 },
 error: function (status, error) {
     console.error(status, error);
 }
});
