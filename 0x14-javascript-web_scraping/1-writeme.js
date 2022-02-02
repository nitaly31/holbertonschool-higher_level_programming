#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(file, stringToWrite, 'utf-8', errorFunc);

function errorFunc (err) {
  if (err) {
    console.log(err);
  }
}
