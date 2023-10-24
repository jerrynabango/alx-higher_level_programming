#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');
request.get(process.argv[2]), 'utf-8'.on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
