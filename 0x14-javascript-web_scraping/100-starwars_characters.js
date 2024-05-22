#!/usr/bin/node

const req = require('request');
const starsApi = 'https://swapi-api.alx-tools.com/api/films/';

req.get(starsApi + process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const films = data.characters;

  for (const film of films) {
    req.get(film, function (error, res, body) {
      if (error) {
        console.log(error);
      }
      const response = JSON.parse(body);
      console.log(response.name);
    });
  }
});
