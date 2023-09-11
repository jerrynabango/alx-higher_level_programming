#!/usr/bin/node

//  function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
	let times = 0;
	while (times < x) {
	  theFunction();
	  times++;
	}
};
