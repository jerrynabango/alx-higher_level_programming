#!/usr/bin/node

//parseInt: function that parses a string and returns a number
const integer = parseInt(process.argv[2]);

if (Number.isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${integer}`);
}
