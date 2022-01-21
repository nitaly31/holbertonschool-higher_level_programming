#!/usr/bin/node
const { argv } = require('process');
if (!argv[2]) {
  console.log('No argument');
} else if (argv[2] && !argv[3]) {
  console.log('Argument found');
} else if (argv[3]) {
  console.log('Arguments found');
}
