#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
//  Star wars API with the endpoint 

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
