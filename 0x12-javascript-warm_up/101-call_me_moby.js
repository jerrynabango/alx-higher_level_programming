#!/usr/bin/node

//  function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
	for (let times = 0; times < x; times++) {
	  theFunction();
	}
};
