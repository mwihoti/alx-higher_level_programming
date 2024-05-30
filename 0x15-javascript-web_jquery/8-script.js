$(document).ready(function() {
    // URL of the API
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  
    // Perform an AJAX GET request to the URL
    $.get(url, function(data) {
      // Get the list of films from the response
      const films = data.results;
      
      // Loop through each film and append the title to the UL element
      for (let i = 0; i < films.length; i++) {
        const title = films[i].title;
        $('<li></li>').text(title).appendTo('ul#list_movies');
      }
    });
  });
  