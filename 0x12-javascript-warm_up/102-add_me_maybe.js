#!/usr/bin/node

// Function that increments and calls a function.

const addMeMaybe = function (number, theFunction) {
	theFunction(++number);
};

module.exports = { addMeMaybe };
