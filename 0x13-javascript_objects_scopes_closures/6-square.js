#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
