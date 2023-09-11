#!/usr/bin/node

/**
 * script that searches the second biggest integer in the list of arguments.
 * You can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */

function searchInteger (list) {
	if (list.length < 2) { return (0); }
	return list.map(Number).sort((x, y) => x - y)[list.length - 2];
}

console.log(searchInteger(process.argv.slice(2)));
