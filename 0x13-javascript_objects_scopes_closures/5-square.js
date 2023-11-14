#!/usr/bin/node
// Class Square defining a square and inheriting from Rectangle
module.exports = class Square extends require('./4-rectangle.js') {
	constructor (size) {
		super(size, size);
	}
};
