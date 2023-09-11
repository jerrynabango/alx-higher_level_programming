#!/usr/bin/node

// Update this script by adding a new function incr that increments the integer value.

const addMeMaybe = function (number, theFunction) {
	theFunction(++number);
};

module.exports = { addMeMaybe };
