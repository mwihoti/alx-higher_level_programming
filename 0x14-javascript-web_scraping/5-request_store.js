#!/usr/bin/node

const req = require('request');
const fs = require('fs');

req(process.argv[2], function (error, res, body) {
  if (error == null) {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(error);
  }
});
