//Wait for the DoM to loa
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
        url: "http://127.0.0.1:5000/api/v1/login",
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify(formData),
        success: function (response) {
            console.log("am here")
           // window.location.href = "register_biz.html";

           $.ajax({
            url: "http://127.0.0.1:5000/api/v1/user_id",
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            xhrFields: {
                withCredentials: true
            },
            success: function (response) {
                console.log("User ID:", response.user_id);
            },
            error: function (xhr, status, error) {
                console.error("Failed to get user ID", status, error);
            }
        });
        
        },
        error: function (xhr, status, error) {
            console.error("Login failed", error);
            console.error("Login failed", xhr, status, error);
        }
    });
   }); 
});