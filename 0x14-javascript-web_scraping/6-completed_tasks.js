#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const completed = {};
    tasks.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});
