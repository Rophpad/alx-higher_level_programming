#!/usr/bin/node
// Class Square defining a square and inheriting from Rectangle
module.exports = class Square extends require('./5-square.js') {
	charPrint(c) {
		if (c === undefined) this.print();
		else {
			for (let i = 0; i < this.height; i++) console.log(c.repeat(this.height));
		}
	}
};
