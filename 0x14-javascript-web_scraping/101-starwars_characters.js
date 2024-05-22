#!/usr/bin/node

const req = require('request');
const swapApi = 'https://swapi-api.hbtn.io/api/films/';

req(swapApi + process.argv[2], function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printName(characters, 0);
  }
});

function printName (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printName(characters, index + 1);
      }
    }
  });
}
