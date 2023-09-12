#!/usr/bin/node

//  class Square that defines a square and inherits from Square of 5-square.js
const ParentSquare = require('./5-square');

// extends: Functions as inheritance from Rectangle
class Square extends ParentSquare {
  charPrint (c = undefined) {
    const shape = c || 'X';
    for (let square1 = 0; square1 < this.height; square1++) {
		let square = '';
		for (let square2 = 0; square2 < this.width; square2++) {
			square += shape;
		}
		console.log(square);
	}
  }
}

module.exports = Square;
