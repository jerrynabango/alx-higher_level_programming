#!/usr/bin/node

// function that returns the reversed version of a list
exports.esrever = function (list) {
	const reverse = [];
	// forEach: used to reverse the list of versions of a list that are not already in the list of versions
	// unshift: used to add the first element to the end of the list and remove from the beginning of the list
	list.forEach(reversedVersion => reverse.unshift(reversedVersion));
	return reverse;
};
