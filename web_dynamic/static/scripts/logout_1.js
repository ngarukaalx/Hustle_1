//Wait for the DOM to load
$(document).ready(function () {
    $("#logout").click(function () {
        // get the current login user id
     let userId;
     $.ajax({
         url: "http://127.0.0.1:5001/api/v1/user_id",
         method: "GET",
         headers: {
             'Content-Type': 'application/json'
         },
         xhrFields: {
             withCredentials: true
         },
         success: function (response) {
             userId = response.user_id;
             console.log(userId)
         },
         error: function (xhr, status, error) {
             console.error("Failed to get user ID", status, error);
         }
     });
     $.ajax({
        url: "http://127.0.0.1:5001/api/v1/logout",
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        xhrFields: {
            withCredentials: true
        },
        success: function (response) {
	    location.reload();
            console.log(response)
        },
        error: function(xhr, status, error) {
            console.error("Failed to logout the current user", status, error);
        }
     });
    });
});
