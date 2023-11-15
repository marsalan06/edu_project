$(document).ready(function() {
    var token_expired_getter = token_expired
        console.log("========t=t==t=====")
        console.log(token_expired_getter)

        if (token_expired_getter == true){
            console.log("=====if condition====")
            $('.create-meeting-button').hide();
            $('.create-session-button').show();
            console.log("-p-p-p-p-")
            
        }
        else if (token_expired_getter == false){
            console.log("=======false else if=======")
            $('.create-session-button').hide();
            $('.create-meeting-button').show();
        }

    $('.create-meeting-button').click(function() {
        
        var teacherId = $(this).data('teacher-id');
        
        // Toggle visibility of input fields, radio buttons, and buttons
        // $('#date-' + teacherId).toggle();
        // $('#time-' + teacherId).toggle();
        // $('#description-' + teacherId).toggle();
        // $('#topic-' + teacherId).toggle();
        // $('.submit-button[data-teacher-id="' + teacherId + '"]').css('display', 'inline-block');
        // $('.cancel-button[data-teacher-id="' + teacherId + '"]').css('display', 'inline-block');
        var dateVisible = $('#date-' + teacherId).is(':visible');
    if (dateVisible) {
        $('#date-' + teacherId).hide();
        $('#time-' + teacherId).hide();
        $('#description-' + teacherId).hide();
        $('#topic-' + teacherId).hide();
        $('.submit-button[data-teacher-id="' + teacherId + '"]').hide();
        $('.cancel-button[data-teacher-id="' + teacherId + '"]').hide();
        $("#expertise-" + teacherId + ":checked").prop("checked", false)

    } else {
        $('#date-' + teacherId).show();
        $('#time-' + teacherId).show();
        $('#description-' + teacherId).show();
        $('#topic-' + teacherId).show();
        $('.submit-button[data-teacher-id="' + teacherId + '"]').show();
        $('.cancel-button[data-teacher-id="' + teacherId + '"]').show();

    }
    });

    $('.submit-button').click(function() {
        console.log("=======testing =====")
        var teacherId = $(this).data('teacher-id');
        var studentId = $('#student-id').val();
        console.log("=====student id--===",studentId)
        var csrf = $("input[name=csrfmiddlewaretoken]").val();
        
        // Get values from input fields
        var date = $('#date-' + teacherId).val();
        var time = $('#time-' + teacherId).val();
        var description = $('#description-' + teacherId).val();
        var topic = $('#topic-' + teacherId).val();
        var expertiseValue = $("#expertise-" + teacherId + ":checked").val();
        console.log("====experties-====",expertiseValue)
        // Make an AJAX request
        var settings = {
            url: "http://0.0.0.0:8000/session/class-sessions/",
            method: "POST",
            timeout: 0,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf
            },
            data: JSON.stringify({
                "teacher": teacherId,
                "student": studentId,
                "date": date,
                "start_time": time,
                "description": description,
                "expertise": expertiseValue,
                "topic": topic,
                // "csrf" : "{% csrf_token %}"
            })
        };
        console.log("======settings====")
        console.log(settings)

        $.ajax(settings).done(function (response) {
            console.log("=====---is susssc=====")
            console.log(response.code)
            console.log(response);
            $('#date-' + teacherId).hide();
        $('#time-' + teacherId).hide();
        $('#description-' + teacherId).hide();
        $('#topic-' + teacherId).hide();
        $('.submit-button[data-teacher-id="' + teacherId + '"]').hide();
        // $('.cancel-button[data-teacher-id="' + teacherId + '"]').hide();
        $("#expertise-" + teacherId + ":checked").prop("checked", false)
        $('.create-meeting-button[data-teacher-id="' + teacherId + '"]').show();
        $('.create-session-button[data-teacher-id="' + teacherId + '"]').hide();

        })
        .fail(function (jqXHR, textStatus, errorThrown) {
            console.log("=====---request failed====");
            console.log("Status Code: " + jqXHR.status);
            console.log("Error: " + errorThrown);
            console.log("Response Text: " + jqXHR.responseText);
            $("#error-message").text("Error: " + Object.keys(JSON.parse(jqXHR.responseText))[0] + ": " + JSON.parse(jqXHR.responseText)[Object.keys(JSON.parse(jqXHR.responseText))[0]]);
            // You can display an error message here or handle the error in your preferred way.
        });
        ;

        // Hide the input fields and buttons
        
    });

    $('.cancel-button').click(function() {
        var teacherId = $(this).data('teacher-id');
        console.log("-----cancle button------")
        console.log(teacherId)
        
        // Hide the input fields and buttons
        $('#date-' + teacherId).hide();
        $('#time-' + teacherId).hide();
        $('#description-' + teacherId).hide();
        $('#topic-' + teacherId).hide();
        $('.submit-button[data-teacher-id="' + teacherId + '"]').css('display', 'none');
        $('.cancel-button[data-teacher-id="' + teacherId + '"]').css('display', 'none');
        $('.create-meeting-button[data-teacher-id="' + teacherId + '"]').show();
        // $('.create-session-button[data-teacher-id="' + teacherId + '"]').show();
        $("#expertise-" + teacherId + ":checked").prop("checked", false)
        // $('#expertise-' + teacherId).hide();
    });
});
