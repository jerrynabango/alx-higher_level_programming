#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const taskCompleted = {};
    tasks.forEach((todo) => {
      if (todo.taskCompleted && taskCompleted[todo.userId] === undefined) {
        taskCompleted[todo.userId] = 1;
      } else if (todo.taskCompleted) {
        taskCompleted[todo.userId] += 1;
      }
    });
    console.log(taskCompleted);
  }
});
