#!/usr/bin/node

/**
 * script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 */

// math.floor: function used to convert a number to an integer value
const square = Math.floor(Number(process.argv[2]));
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let arg1 = 0; arg1 < square; arg1++) {
    let sizeOfSquare = '';
    for (let arg2 = 0; arg2 < square; arg2++) sizeOfSquare += 'X';
    console.log(sizeOfSquare);
  }
}
