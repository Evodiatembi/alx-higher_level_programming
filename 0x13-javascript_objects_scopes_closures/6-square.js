#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let k = 0; k < this.height; k++) {
      let a = '';
      for (let m = 0; m < this.width; m++) {
        a += c;
      }
      console.log(a);
    }
  }
}

module.exports = Square;
