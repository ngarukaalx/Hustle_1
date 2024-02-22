//Wait for the DoM to load
//This code performs login of a register user
console.log("Before form submission");
$(document).ready(function () {
   $("#login-form").submit(function (event) {
    console.log("Form submitted");
    event.preventDefault(); // prevent the form from submiting traditionally

    // get form data
    const formData = {
        email: $("#email").val(),
        password: $("#password").val()
    };
    console.log(formData);
    // send post request
    $.ajax({
        url: "http://127.0.0.1:5001/api/v1/login",
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        xhrFields: {
             withCredentials: true
        },
        data: JSON.stringify(formData),
        success: function (response) {
           console.log(response);
           // get the current user id of the login user
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
		alert("Login successful");
                userId = response.user_id;
                // get the business of this user if no available business direct to businesss creation page
                // else direct to business page
                $.ajax({
                    url: "http://127.0.0.1:5001/api/v1/business/" + userId,
                    method: "Get",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    success: function (response) {
			window.location = "user_page";
                    },
                    error: function(status, error) {
                        window.location = "register-biz";
                    }
                });
            },
            error: function (xhr, status, error) {
                console.error("Failed to get user ID", status, error);
            }
        });
        },
        error: function (xhr, status, error) {
	    location.reload();
            alert("Wrong email or password!");
            console.error("Login failed", error);
            console.error("Login failed", xhr, status, error);
        }
    });
   });
});
