const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    request.get(i, (error, res, body) => {
      if (error) {
        console.log(error);
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
