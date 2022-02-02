#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

let dicFilms = {};
let count = 0;

request(url, errorFunc);

function errorFunc (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    dicFilms = JSON.parse(body);
    for (let i = 0; i < dicFilms.results.length; i++) {
      for (let j = 0; j < dicFilms.results[i].characters.length; j++) {
        if (dicFilms.results[i].characters[j].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
}
