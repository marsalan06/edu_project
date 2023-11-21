$(document).ready(function () {
    var token_expired_getter = token_expired;
    console.log("========t=t==t=====");
    console.log(token_expired_getter);

    if (token_expired_getter == true) {
        console.log("=====if condition====");
        $('.create-meeting-button').hide();
        $('.create-session-button').show();
        console.log("-p-p-p-p-");
    } else if (token_expired_getter == false) {
        console.log("=======false else if=======");
        $('.create-session-button').hide();
        $('.create-meeting-button').show();
    }

    $('.create-meeting-button').click(function () {
        var teacherId = $(this).data('teacher-id');

        var dateVisible = $('#date-' + teacherId).is(':visible');
        if (dateVisible) {
            $('#date-' + teacherId).hide();
            $('#time-' + teacherId).hide();
            $('#description-' + teacherId).hide();
            $('#topic-' + teacherId).hide();
            $('.submit-button[data-teacher-id="' + teacherId + '"]').hide();
            $('.cancel-button[data-teacher-id="' + teacherId + '"]').hide();
            $("#expertise-" + teacherId + ":checked").prop("checked", false);
        } else {
            $('#date-' + teacherId).show();
            $('#time-' + teacherId).show();
            $('#description-' + teacherId).show();
            $('#topic-' + teacherId).show();
            $('.submit-button[data-teacher-id="' + teacherId + '"]').show();
            $('.cancel-button[data-teacher-id="' + teacherId + '"]').show();
        }
    });

    $('.submit-button').click(function () {
        console.log("=======testing =====");
        var teacherId = $(this).data('teacher-id');
        var studentId = $('#student-id').val();
        var csrf = $("input[name=csrfmiddlewaretoken]").val();

        var date = $('#date-' + teacherId).val();
        var time = $('#time-' + teacherId).val();
        var description = $('#description-' + teacherId).val();
        var topic = $('#topic-' + teacherId).val();
        var expertiseValue = $("#expertise-" + teacherId + ":checked").val();
        console.log("====experties-====", expertiseValue);

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
            })
        };

        console.log("======settings====");
        console.log(settings);

        function makeSecondRequest(data) {
            return new Promise(function (resolve, reject) {
                var meeting_req = {
                    url: 'http://0.0.0.0:8000/zoom/meeting/',
                    method: 'POST',
                    timeout: 0,
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrf
                    },
                    data: JSON.stringify({
                        teacherId: data.teacher,
                        studentId: data.student,
                        topic: data.topic,
                        start_time: data.start_time,
                        date: data.date,
                        teaching_session: data.id
                    })
                };
                console.log("======meeting request====");
                console.log(meeting_req);

                $.ajax(meeting_req).then(function (meetingData, meetingTextStatus, meetingXhr) {
                    console.log('Meeting created successfully:', meetingData);
                    resolve();
                }).fail(function (meetingJqXHR, meetingTextStatus, meetingErrorThrown) {
                    console.log("=====---second request failed====");
                    console.log("Status Code: " + meetingJqXHR.status);
                    console.log("Error: " + meetingErrorThrown);
                    console.log("Response Text: " + meetingJqXHR.responseText);
                    reject(meetingErrorThrown);
                    $('.error-message[data-teacher-id="' + teacherId + '"]').text("Error: " + Object.keys(JSON.parse(jqXHR.responseText))[0] + ": " + JSON.parse(jqXHR.responseText)[Object.keys(JSON.parse(jqXHR.responseText))[0]]);


                });
            });
        }

        $.ajax(settings).then(function (data, textStatus, xhr) {
            console.log("=----oooo---");
            if (xhr.status == 201) {
                console.log("=====successiiiisisi-----");

                // Make the second AJAX call and wait for it to complete
                return makeSecondRequest(data);
            }
        }).then(function () {
            console.log("=====---is success=====");
            $('#date-' + teacherId).hide();
            $('#time-' + teacherId).hide();
            $('#description-' + teacherId).hide();
            $('#topic-' + teacherId).hide();
            $('.submit-button[data-teacher-id="' + teacherId + '"]').hide();
            $("#expertise-" + teacherId + ":checked").prop("checked", false);
            $('.cancel-button[data-teacher-id="' + teacherId + '"]').hide();
            $('.create-meeting-button[data-teacher-id="' + teacherId + '"]').show();
            $('.create-session-button[data-teacher-id="' + teacherId + '"]').hide();
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
        console.log("=====---first request failed====");
        console.log("Status Code: " + jqXHR.status);
        console.log("Error: " + errorThrown);
        console.log("Response Text: " + jqXHR.responseText);
        $('.error-message[data-teacher-id="' + teacherId + '"]').text("Error: " + Object.keys(JSON.parse(jqXHR.responseText))[0] + ": " + JSON.parse(jqXHR.responseText)[Object.keys(JSON.parse(jqXHR.responseText))[0]]);
    });
});



    $('.cancel-button').click(function () {
        var teacherId = $(this).data('teacher-id');
        console.log("-----cancle button------");
        console.log(teacherId);

        $('#date-' + teacherId).hide();
        $('#time-' + teacherId).hide();
        $('#description-' + teacherId).hide();
        $('#topic-' + teacherId).hide();
        $('.submit-button[data-teacher-id="' + teacherId + '"]').css('display', 'none');
        $('.cancel-button[data-teacher-id="' + teacherId + '"]').css('display', 'none');
        $('.create-meeting-button[data-teacher-id="' + teacherId + '"]').show();
        $("#expertise-" + teacherId + ":checked").prop("checked", false);
    });
});
