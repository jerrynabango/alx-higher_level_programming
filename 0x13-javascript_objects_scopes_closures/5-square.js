#!/usr/bin/node

// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
const Rectangle = require('./4-rectangle');

// extends: Functions as inheritance from Rectangle
class Square extends Rectangle {
  constructor (size) {
	// super: used to access properties on an object literal or class's [[Prototype]],or invoke a superclass's constructor.
    super(size, size);
  }
}

module.exports = Square;
