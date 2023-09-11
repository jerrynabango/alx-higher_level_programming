#!/usr/bin/node

// function that increments and calls a function.

const addMeMaybe = function (number, theFunction) {
	theFunction(++number);
};

module.exports = { addMeMaybe };
