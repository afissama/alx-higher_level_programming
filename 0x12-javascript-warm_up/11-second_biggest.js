#!/usr/bin/node
const argv = process.argv
let xMax = 0
let xSecond = 0
if (argv.length > 3) {
  xMax = argv[2]
  xSecond = argv[2]
  for (let i = 3; i < argv.length; i++) {
    const curnt = Number(argv[i])
    if (curnt > xMax) {
      xSecond = xMax
      xMax = curnt
      continue
    }
    if (curnt > xSecond) { xSecond = curnt }
  }
}
console.log(xSecond)
