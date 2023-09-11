#!/usr/bin/node

/**
 * script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurrences”
 */

const x = process.argv[2];

let argument = 0;
while (argument < x) {
  console.log('C is fun');
  argument++;
}
