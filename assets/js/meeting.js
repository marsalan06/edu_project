// JavaScript function to open Zoom authentication and extract the access code

  $(document).ready(function() {
    $('.create-meeting-button').click(function() {
        // Send a request to the Zoom OAuth URL
        $.ajax({
            url: 'http://0.0.0.0:8000/zoom/oauth/redirect/',
            dataType: 'json',
            success: function(data) {
                if (data.access_token) {
                    // Send the access code to your API
                    $.ajax({
                        url: 'http://0.0.0.0:8000/zoom/meeting/',
                        type: 'POST',
                        contentType: 'application/json',
                        data: JSON.stringify({ access_token: data.access_token }),
                        success: function(response) {
                            console.log(response);
                            // Handle the response here
                        },
                        error: function(error) {
                            console.error(error);
                        }
                    });
                } else {
                    console.error('Access token not received');
                }
            },
            error: function(error) {
                console.error(error);
            }
        });
    });
});
