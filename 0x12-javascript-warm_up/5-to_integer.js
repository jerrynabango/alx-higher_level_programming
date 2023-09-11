#!/usr/bin/node

/**
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
 */

//parseInt: function that parses a string and returns a number
const arg = parseInt(process.argv[2]);

// Using template literal
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
