#!/usr/bin/node
exports.converter = function (base) {
	return (num) {
		return num.toString(base);
	};
};
