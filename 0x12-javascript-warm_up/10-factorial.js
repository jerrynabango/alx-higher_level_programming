#!/usr/bin/node

/**
 * script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 */

function factorial (arr) {
	if (isNaN(arr) || arr === 1) { return (1); }
	return arr * factorial(arr - 1);
}
  
console.log(factorial(process.argv[2]));
