#!/usr/bin/node

/**
 * script that prints the first argument passed to it:
 * If no arguments are passed to the script, print “No argument”
 * You must use console.log(...) to print all output
 */

const valueOfArgument = process.argv[2];

if (valueOfArgument) {
	console.log(valueOfArgument);
} else (valueOfArgument === undefined) {
	console.log(`No argument`);
}
