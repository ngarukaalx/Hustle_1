// wait for the DOM to load
$(document).ready(function () {
    $.ajax({
        url: "http://127.0.0.1:5001/api/v1/counties",
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        },
        success: function(data) {
            // Get select element
        const select = $("#selectcounty");
        //Iterate through the data to create options
        $.each(data, function(index, county) {
            select.append("<option value='" + county.id + "'>" + county.name + "</option>");
        });
        }
    });
    $.ajax({
        url: "http://127.0.0.1:5001/api/v1/towns",
        method: "GET",
        headers: {
            'Content-Type': 'application/json'
        },
        success: function(data) {
            // Get select element
        const select = $("#town");
        //Iterate through the data to create options
        $.each(data, function(index, town) {
            select.append("<option value='" + town.id + "'>" + town.name + "</option>");
        });
        }
    });
});
