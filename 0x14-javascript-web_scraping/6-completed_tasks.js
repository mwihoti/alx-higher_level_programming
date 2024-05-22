#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, res, body) => {
  const numTasks = {};
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  json.forEach(task => {
    if (task.completed) {
      if (!numTasks[task.userId]) {
        numTasks[task.userId] = 0;
      }
      numTasks[task.userId]++;
    }
  });
  console.log(numTasks);
});
