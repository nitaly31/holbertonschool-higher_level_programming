#!/usr/bin/node
const { argv } = require('process');
if (!argv[3]) {
  console.log(0);
} else if (argv[2] && argv[3] && argv[2] === argv[3]) {
  console.log(0);
} else if (argv[2] && argv[3]) {
  const unique = [...new Set(argv)];
  function comparar (a, b) {
    return (a - b);
  }
  unique.sort(comparar);
  const number = unique.length;
  console.log(parseInt(unique[number - 2]));
}
