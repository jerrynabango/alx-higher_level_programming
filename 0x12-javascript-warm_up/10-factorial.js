#!/usr/bin/node 

/**
 * script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 */

function factorial (n) {
	if (isNaN(n) || n === 1) { return (1); }
	return n * factorial(n - 1);
  }
  
console.log(factorial(process.argv[2]));
