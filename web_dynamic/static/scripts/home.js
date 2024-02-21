//wait for the DOM to load
$(document).ready(function () {
  $.ajax({
    url: "http://127.0.0.1:5001/api/v1/biz/",
    method: "GET",
    headers: {
      'Content-Type': 'application/json' 
    },
    success: function (data) {
      // Define a fuction to fetch video details asynchronously
      async function fetchVideoDetailsAsync(businessId) {
        try {
          const response = await $.ajax({
            url: `http://127.0.0.1:5001/api/v1/businesses/${businessId}/videos`,
            method: "GET",
            headers: {
              'Content-Type': 'application/json'
            },
          });
          return response.length > 0 ? response[0] : null;

        } catch (error) {
          console.error('Error fetching video details:', error);
          throw error;
        }
      }
      // Use async/wait inside the loop
      $.each(data, async function (index, biz) {
        if (biz.business_videos.length == 0) {
          return true;
        }
        try {
          const videoDetails = await fetchVideoDetailsAsync(biz.id);
          console.log('Business name: ', biz.name);
	  console.log('countyName', biz.county_name);
	  console.log('TownNmae', biz.town_name);
          console.log('video url:', videoDetails.url);
	  console.log('video description', videoDetails.description);
	  const sec1 = $('<section>').addClass('biz');
	  const divLogo = $('<div>').addClass('biz-logo');
	  const img = $('<img>');
	  const logoUrl = "http://127.0.0.1:5001/api/v1/uploads/" + biz.logo
	  img.attr({
		  src: logoUrl,
		  alt: 'logo'
	  });
	  divLogo.append(img);
	  const divLocation = $('<div>').addClass('biz-info');
	  const h2 = $('<h2>').text(biz.name)
	  const p = $('<p>').text('County: ' + biz.county_name);
	  const p1 = $('<p>').text('Town: ' + biz.town_name);
	  divLocation.append(h2, p, p1);
	  sec1.append(divLogo, divLocation);
	  const divD = $('<div>').addClass('description');
	  const p2 = $('<p>').text(videoDetails.description);
	  divD.append(p2);
	  const vid = $('<video controls>');
	  vidUrl = "http://127.0.0.1:5001/api/v1/uploads/" + videoDetails.url
	  const source = $('<source>').attr({
		  src: vidUrl,
		  type: 'video/mp4'
	  });
	  vid.append(source);
	  const secButton = $('<section>').addClass('vid-bottom');
	  const divInfor = $('<div>').addClass('vid-info');
	  const btn1 = $('<button>').addClass('btn-fisrt');
          btn1.text('comment');
	  const btn2 = $('<button>').addClass('btn-second');
	  btn2.text('message')
	  divInfor.append(btn1, btn2);
	  const divUserpage = $('<div>').addClass('biz-data');
	  const a = $('<a>').attr({
		  href: '#'
	  });
	  const btn3 = $('<button>').addClass('btn-third');
	  btn3.text('More');
	  a.append(btn3);
	  divUserpage.append(a);
	  secButton.append(divInfor, divUserpage);
	  //set the businessid as data
	  btn3.data('bizData', biz.id);
	  btn3.click(function () {
		  //retrive the business_id when the button is clicked
		  const bizId = $(this).data('bizData');
		  //redirect to the user page using the business_id
		  window.location.href = 'user_page?bizData=' + bizId
	  });
	  const refine = $('<section>').addClass('refine');
	  refine.prepend(sec1, divD, vid, secButton);
	  $('.container.busines-section').append(refine);
	  
        } catch (error) {
          console.error('Error in iteration:', error);
        }
      });
    },
    error: function (status, error) {
      console.error(status, error);
    }
  });
});
