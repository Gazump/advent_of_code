import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const convertToArray = (packet: string): any[] => {
  return JSON.parse(packet);
}

const compare = (left: any, right: any): boolean | undefined => {
  if (Array.isArray(left) && Array.isArray(right)) {
    for (let i = 0 ; i < left.length ; i++) {
      if (i >= right.length) {
        return false;
      }
      const comparison = compare(left[i], right[i]);
      if (comparison !== undefined) {
        return comparison;
      }
    }
    if (right.length > left.length) {
      return true;
    }
  } else if (Array.isArray(left) && !isNaN(right)) {
    return compare(left, [right]);
  } else if (Array.isArray(right) && !isNaN(left)) {
    return compare([left], right);
  } else {
    // numbers
    return left === right ? undefined : left < right;    
  }
  return undefined;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  let sum = 0;

  for( let i = 1; i <= input.length ; i+=3 ) {
    const packet1 = convertToArray(input[i-1]);
    const packet2 = convertToArray(input[i]);
    
    if (compare(packet1, packet2)) {
      sum+=(i + 2)/3;
    }
  }

  return sum.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const array = [[[2]],[[6]]];

  for( let i = 1; i <= input.length ; i+=3 ) {
    array.push(convertToArray(input[i-1]));
    array.push(convertToArray(input[i]));
  }

  array.sort((left,right) => {
    const comparison = compare(left,right);

    return comparison === undefined ? 0 : comparison ? -1 : 1;    
  });

  let multiple = 1;

  for( let i = 1; i <= array.length ; i++ ) {
    if( JSON.stringify(array[i-1]) === JSON.stringify([[2]]) || JSON.stringify(array[i-1]) === JSON.stringify([[6]])) {
      multiple *= i;
    }
  }

  return multiple.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          [1,1,3,1,1]
          [1,1,5,1,1]
          
          [[1],[2,3,4]]
          [[1],4]
          
          [9]
          [[8,7,6]]
          
          [[4,4],4,4]
          [[4,4],4,4,4]
          
          [7,7,7,7]
          [7,7,7]
          
          []
          [3]
          
          [[[]]]
          [[]]
          
          [1,[2,[3,[4,[5,6,7]]]],8,9]
          [1,[2,[3,[4,[5,6,0]]]],8,9]
        `,
        expected: "13",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          [1,1,3,1,1]
          [1,1,5,1,1]
          
          [[1],[2,3,4]]
          [[1],4]
          
          [9]
          [[8,7,6]]
          
          [[4,4],4,4]
          [[4,4],4,4,4]
          
          [7,7,7,7]
          [7,7,7]
          
          []
          [3]
          
          [[[]]]
          [[]]
          
          [1,[2,[3,[4,[5,6,7]]]],8,9]
          [1,[2,[3,[4,[5,6,0]]]],8,9]
        `,
        expected: "140",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
