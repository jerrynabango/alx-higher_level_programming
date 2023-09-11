#!/usr/bin/node

function factorial (integer) {
	if (isNaN(integer) || integer === 1) { return (1); }
	return integer * factorial(integer - 1);
  }
  
console.log(factorial(process.argv[2]));
