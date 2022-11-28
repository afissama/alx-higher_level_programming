#!/usr/bin/node
const argv = process.argv

if (isNaN(Number(argv[2]))) {
  console.log('Not a number')
} else {
  console.log('My number: ' + argv[2])
}
