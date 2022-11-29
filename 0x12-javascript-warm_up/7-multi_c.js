#!/usr/bin/node
const argv = process.argv;

if (argv.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  let x = argv[2];
  while (x > 0) {
    console.log('C is fun');
    x = x - 1;
  }
}
