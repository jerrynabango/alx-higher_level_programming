#!/usr/bin/node

/**
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
 */

// parseInt: Function used to parse a string into a number
const myNumber = parseInt(process.argv[2]);

if (Number.isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNumber}`);
}
