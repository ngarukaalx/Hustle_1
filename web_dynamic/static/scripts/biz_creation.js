// Wait for the DOM to load
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
		console.log("heywhatswrong");
        },
        error: function (xhr, status, error) {
            console.error("Failed to get user ID", status, error);
        }
    });

    // Attach an event listener
    $("#biz-form").submit(function (event) {
        event.preventDefault(); // prevent the form from submitting traditionally

        // get form data
        const formData = {
            county_id: $("#selectcounty").val(),
            town_id: $("#town").val(),
            name: $("#biz-name").val(),
            description: $("#type").val(),
            exact_location: $("exact").val()
        };

        if (userId) {
            formData.user_id = userId;
        } else {
            console.log("UserId not available");
            return;
        }
        // create the formdata for the logo file
        const fileInput = document.getElementById('logo');
        let fileFormData = new FormData();
        let file = fileInput.files[0];
        if (file) {
	    console.log("Am here")
            fileFormData.append('file', file);
        }
	console.log(fileFormData);

        // Send data as JSON to create a business
        $.ajax({
            url: "http://127.0.0.1:5001/api/v1/createbiz",
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify(formData),
            success: function (response) {
		// creates a logo if business creation was success and relate it to its business
                const business_id = response.id;
                if (file) {
                    fileFormData.append('business_id', business_id)
		    // send form data to the server
		    $.ajax({
			    url: "http://127.0.0.1:5001/api/v1/uploadlogo",
			    method: "POST",
			    processData: false,
			    contentType: false,
			    data: fileFormData,
			    success: function (response) {
				    console.log(response);
				    // shirt window to business page after succesfull creation of business and logo
				    // and get the businesss created 
				    window.location.href = "user_page";
			    },
			    error: function (xhr, status, error) {
				    console.log(status, error)
			    }
		    });
                }else{
		     // shirt window to business created page if no file was provided
		     window.location.href = "user_page";
		}
            },
            error: function (xhr, status, error) {
                console.error(status, error);
            }
        });
    });
});
