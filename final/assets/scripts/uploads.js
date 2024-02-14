$(document).ready(function() {
    // Show the modal when the upload button is clicked
    $(".uploads").click(function() {
      $(".overlay").show();
    });

    // Close the modal when the close button is clicked
    $("#closeModal").click(function() {
      $(".overlay").hide();
    });

    // Submit the form when the Upload button is clicked
    $("#uploadForm").submit(function(event) {
      event.preventDefault();

      // Handle form submission (you can use AJAX to send the form data to the server)
      // ...

      // Close the modal
      $(".overlay").hide();
    });
  });