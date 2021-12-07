/** 
 * @author nbosh 
 * @description Advent of Code 2021 - Problem 1_a
 * @version 1.0
*/

const fs = require('fs');
const path = require('path');

const lines = String(fs.readFileSync(path.join(__dirname, "/../input_1.txt"))).split(require("os").EOL).map(Number);

console.log(lines.filter((num, index, nums) => num > nums[index-1]).length);

