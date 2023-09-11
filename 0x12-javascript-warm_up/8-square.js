#!/usr/bin/node

/**
 * script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 */

// math.floor: function used to convert a number to an integer value
const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing square');
} else {
  let arg1 = 0;
  while (arg1 < size) {
    let sizeOfSquare = '';
    let arg2 = 0;
    while (arg2 < size) {
      sizeOfSquare += 'X';
      arg2++;
    }
    console.log(sizeOfSquare);
    arg1++;
  }
}
