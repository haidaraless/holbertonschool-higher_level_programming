#!/usr/bin/node
function factorial (n) {
  if (!parseInt(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return factorial(n - 1) * n;
}
console.log(factorial(process.argv[2]));
