#!/usr/bin/node

const req = require('request');
const res = 'https://swapi-api.alx-tools.com/api/films/';

req.get(res + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
