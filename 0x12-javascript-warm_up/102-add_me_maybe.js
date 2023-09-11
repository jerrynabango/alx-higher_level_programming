#!/usr/bin/node

// Update this script by adding a new function incr that increments the integer value.

exports.addMeMaybe = function (number, theFunction) {
	theFunction(++number);
};
