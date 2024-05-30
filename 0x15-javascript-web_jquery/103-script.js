$(document).ready(function() {
    function fetchTranslation() {
      // Get the value of the input field
      const langCode = $('#language_code').val();
  
      // Construct the API URL
      const url = `https://www.fourtonfish.com/hellosalut/hello/`;
  
      // Perform an AJAX GET request to the URL
      $.get(url, function(data) {
        // Display the translation in the DIV#hello
        $('#hello').text(data.hello);
      });
    }
  
    // Fetch translation when the button is clicked
    $('#btn_translate').click(fetchTranslation);
  
    // Fetch translation when Enter key is pressed while focusing on the input field
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // 13 is the keycode for Enter
        fetchTranslation();
      }
    });
  });
  