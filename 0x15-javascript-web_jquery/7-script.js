//  JavaScript script that fetches the character name
const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (res) {
    $('#character').append(res.name);
})