#!/usr/bin/node

/**
 * A script that prints a message depending on the number of arguments passed:
 * If no arguments are passed to the script, it prints "No argument."
 * If only one argument is passed to the script, it prints "Argument found."
 * Otherwise, it prints "Arguments found."
 */

const numberOfArguments = process.argv.length - 2;
// Strict Equality comparison (===)
if (numberOfArguments === 0) {
	console.log('No argument');
} else if (numberOfArguments === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
