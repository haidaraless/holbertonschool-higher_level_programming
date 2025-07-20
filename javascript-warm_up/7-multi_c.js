#!/usr/bin/node
const times = process.argv[2];

if (!parseInt(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(times); i++) {
    console.log('C is fun');
  }
}
