#!/usr/bin/node
const argv = process.argv

function fact (n) {
  if (n < 0) { return }
  if (n === 0 || isNaN(n)) { return 1 }
  return n * fact(n - 1)
}
console.log(fact(Number(argv[2])))
