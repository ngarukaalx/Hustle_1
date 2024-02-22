//wait for the DOM to load
$(document).ready(function () {
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
             updateUI(userId);
	     // update the user page with the the business related to this user
         },
         error: function (xhr, status, error) {
	     updateUI(userId);
             console.error("Failed to get user ID", status, error);
         }
     });
     //function to update the login and logout button on the availability of userId
     function updateUI(userId) {
        const logout = $("#logout");
        const login = $("#login");
        if (userId) {
            logout.css("display", "block");
            login.css("display", "none");
        }else{
            login.css("display", "block");
            logout.css("display", "none");
        }
     }
});
