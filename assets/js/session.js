$(document).ready(function() {
    $('.create-session-button').click(function() {
        var teacherId = $(this).data('teacher-id');
        
        // Toggle visibility of input fields, radio buttons, and buttons
        $('#date-' + teacherId).toggle();
        $('#time-' + teacherId).toggle();
        $('#description-' + teacherId).toggle();
        $('#topic-' + teacherId).toggle();
        $('.submit-button[data-teacher-id="' + teacherId + '"]').css('display', 'inline-block');
        $('.cancel-button[data-teacher-id="' + teacherId + '"]').css('display', 'inline-block');
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
            console.log(response);
        });

        // Hide the input fields and buttons
        $('#date-' + teacherId).hide();
        $('#time-' + teacherId).hide();
        $('#description-' + teacherId).hide();
        $('#topic-' + teacherId).hide();
        $('#submit-' + teacherId).hide();
        $('#cancel-' + teacherId).hide();
    });

    $('.cancel-button').click(function() {
        var teacherId = $(this).data('teacher-id');
        
        // Hide the input fields and buttons
        $('#date-' + teacherId).hide();
        $('#time-' + teacherId).hide();
        $('#description-' + teacherId).hide();
        $('#topic-' + teacherId).hide();
        $('.submit-button[data-teacher-id="' + teacherId + '"]').css('display', 'none');
        $('.cancel-button[data-teacher-id="' + teacherId + '"]').css('display', 'none');
        // $('#expertise-' + teacherId).hide();
    });
});
