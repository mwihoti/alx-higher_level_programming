#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
