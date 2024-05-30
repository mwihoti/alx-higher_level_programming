$(document).ready(function() {
    // URL of the API
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    
    $.get(url, function(data) {
      // Get the translation 
      const hello = data.hello;
  
   
      $('div#hello').text(hello);
    });
  });