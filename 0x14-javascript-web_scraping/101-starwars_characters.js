#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const film = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(film, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    Characters(characters, 0);
  }
});

function Characters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        Characters(characters, index + 1);
      }
    }
  });
}
