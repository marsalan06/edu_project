// var script = document.createElement('script');
// script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.js';
// document.body.appendChild(script);

$(document).ready(function() {
    // Get the select field elements
    var $teacherSelect = $('#id_teacher');
    var $expertiseSelect = $('#id_expertise');
  
    // Function to update the expertise choices
    function updateExpertiseChoices() {
      // Get the selected teacher's ID
      var teacherId = $teacherSelect.val();
      console.log("===========7777====")
      console.log(teacherId)
  
      // Make an AJAX request to retrieve the expertise choices for the selected teacher
      $.ajax({
        method: 'GET',
        url: '/session/choices/',
        data: { teacher_id: teacherId },
        // url: '0.0.0.0:8000/session/choices/?teacher_id='+teacherId,
        // data: { teacher_id: teacherId },
        success: function(data) {
          console.log("=========testing====")
          console.log(data)
          // Clear the expertise select field
          $expertiseSelect.empty();
  
          // Add the retrieved expertise choices as options
          $.each(data.choices, function(index, choice) {
            console.log(choice)
            $expertiseSelect.append($('<option>').val(choice).text(choice));
          });
        },
        error: function() {
          console.log('Error occurred while retrieving expertise choices.');
        }
      });
    }
  
    // Attach event listener to the teacher select field
    $teacherSelect.on('change', function() {
      updateExpertiseChoices();
    });
  
    // Initialize expertise choices on page load
    updateExpertiseChoices();
  });
  