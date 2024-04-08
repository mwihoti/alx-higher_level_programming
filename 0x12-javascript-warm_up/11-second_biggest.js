#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const big = process.argv.sort();
  console.log(big.reverse()[1]);
}
