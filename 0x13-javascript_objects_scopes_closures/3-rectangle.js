#!/usr/bin/node

// class Rectangle that defines a rectangle
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
  
	print () {
		for (let arg1 = 0; arg1 < this.height; arg1++) {
			let shape = '';
			for (let arg2 = 0; arg2 < this.width; arg2++) {
				shape += 'X';
			}
			console.log(shape);
		}
	}
}

module.exports = Rectangle;
