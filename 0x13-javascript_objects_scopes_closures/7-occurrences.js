#!/usr/bin/node

// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
	let numberOfOccurrences = 0;
	for (let number = 0; number < list.length; number++) {
		if (searchElement === list[number]) {
			numberOfOccurrences++;
		}
	}
	return numberOfOccurrences;
};
