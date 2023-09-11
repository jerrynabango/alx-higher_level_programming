#!/usr/bin/node

/**
 *  script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 */

const [a, b] = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
