#!/usr/bin/node

// script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
const sort = {};
for (const [id1, id2] of Object.entries(dict)) {
	if (sort[id2] === undefined) {
		sort[id2] = [id1];
	} else {
		sort[id2].push(id1);
	}
}

console.log(sort);
