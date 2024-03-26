#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;

    let numOfMovies = 0;

    films.foeEach((film) => {
      const characters = films.characters;
      if (characters.inlcudes('https://swapi-api.alx-tools.com/api/people/18/')) {
        numOfMovies++;
      }
    });

    console.log(`Number of movies where "Wedge Antilles" is present: ${numOfMovies}`);
  } else {
    console.error('Error:', error);
  }
});
