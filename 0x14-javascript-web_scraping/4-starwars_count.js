#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (body) {
    const json = JSON.parse(body);
    const films = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(films.length);
  }
});
