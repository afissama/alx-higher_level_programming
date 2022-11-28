#!/usr/bin/node
const argv = process.argv

if (isNaN(Number(argv[2]))) {
  console.log('Missing size')
} else {
  const x = argv[2]
  for (let i = 0; i < x; i++) {
    let tmp = ''
    for (let j = 0; j < x; j++) {
      tmp = tmp + 'X'
    }
    console.log(tmp)
  }
}
