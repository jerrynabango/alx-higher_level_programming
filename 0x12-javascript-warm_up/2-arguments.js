#!/usr/bin/node

/**
* script that prints a message depending of the number of arguments passed:
* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
*/

// Strict Equality comparison (===)
const numberOfArguments = process.argv.length - 2;
if (numberOfArguments === 0) {
	console.log('No argument');
} else if (numberOfArguments === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
