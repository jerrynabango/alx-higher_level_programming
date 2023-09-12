#!/usr/bin/node

// script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
const sort = {};
for (const [numberOfOccurrences, userIds] of Object.entries(dict)) {
	if (sort[userIds] === undefined) {
    sort[userIds] = [numberOfOccurrences];
  } else {
	sort[userIds].push(numberOfOccurrences);
  }
}

console.log(sort);
