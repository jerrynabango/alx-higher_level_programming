#!/usr/bin/node

// script that prints two arguments passed to it, in the following format: “ is ”

const argument = process.argv.slice(2);
console.log(`${argument[0]} is ${argument[1]}`);
