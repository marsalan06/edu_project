$(document).ready(function() {
    var oauthRedirectUrl = '/oauth/redirect/';

    $('#createMeetingButton').on('click', function() {
        // Make an AJAX request to the server for redirection
        $.ajax({
            type: 'GET',
            url: '/zoom/oauth-method/',
            success: function(response) {
                // Handle success, e.g., open the returned URL in a new tab
                window.open(response.redirectUrl, '_blank');
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});
