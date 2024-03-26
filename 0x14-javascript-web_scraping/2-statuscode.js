#!/usr/bin/node
const request = require('request');
request.get((process.argv[2]), (res, error) => {
  if (error) {
    console.log('error: ', error);
  }
  console.log(`code: ${res.statusCode}`);
});
