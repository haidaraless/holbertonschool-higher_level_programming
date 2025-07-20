#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < args.length; i++) {
    array.push(args[i]);
  }
  array.sort(function (a, b) { return b - a; });
  console.log(array[1]);
}
