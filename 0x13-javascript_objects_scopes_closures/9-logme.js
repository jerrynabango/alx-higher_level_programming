#!/usr/bin/node

// function that prints the number of arguments already printed and the new argument value
let numberOfArgs = 0;

exports.logMe = function (item) {
	// using template literal 
	console.log(`${numberOfArgs++}: ${item}`);
};
