#!/usr/bin/node

/**
 * script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 */

function factorial (integer) {
	if (isNaN(integer) || integer === 1) { return (1); }
	return integer * factorial(integer - 1);
}
  
console.log(factorial(process.argv[2]));
