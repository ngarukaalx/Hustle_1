// Wait for the DOM to load
// This a code to perform signing or register a user
$(document).ready(function () {
    //Attach an event listener
    $("#signup-form").submit(function (event) {
        event.preventDefault(); // prevent the form from submiting traditionally
         // get form data
    const formData = {
        county_id: $("#selectcounty").val(),
        town_id: $("#town").val(),
        first_name: $("#first").val(),
        last_name: $("#second").val(),
        email: $("#mail").val(),
        password: $("#pass").val()
    };
    // Creates a user
    $.ajax({
        url: "http://127.0.0.1:5001/api/v1/users",
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify(formData),
        success: function(response) {
            console.log("API Response:", response);
        },
        error: function (xhr, status, error) {
            console.error(status, error);
        }
    });
    });
});
