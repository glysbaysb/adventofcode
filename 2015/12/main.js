const input = require('./input.json');


function sumNumbers(obj) {
	let sum = 0;
	for(idx in obj) {
		if(typeof obj[idx] === 'object') {
			sum += sumNumbers(obj[idx]);
		} else if(typeof obj[idx] === 'number') {
			sum += obj[idx];
		} else if(typeof obj[idx] === 'string') {
			sum += sumNumbers(obj[idx]);
		}
	}

	return sum;
}

console.log(sumNumbers(input));
