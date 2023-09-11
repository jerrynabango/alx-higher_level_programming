#!/usr/bin/node

/**
 * script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 */

if (process.argv.length < 2) {
	console.log(0);
} else {
	const list = process.argv.map(Number)
	  .slice(2, process.argv.length)
	  .sort((a, b) => a - b);
	console.log(list[list.length - 2]);
}
