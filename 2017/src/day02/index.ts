import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");

  let output = 0;
  input.forEach((line) => {
    const nums = line.split("\t").map((string) => parseInt(string));
    output += Math.max(...nums) - Math.min(...nums);
  });

  return output.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");

  let output = 0;
  input.forEach((line) => {
    const nums = line.split("\t").map((string) => parseInt(string));
    
    nums.forEach((num) => {
      const other = nums.find((otherNum) => num != otherNum && num % otherNum == 0);
      if (other) {
        output += num / other;
      }
    });
  });

  return output.toString();
};

run({
  part1: {
    tests: [
      // {
      //   input: ``,
      //   expected: "",
      // },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          5\t9\t2\t8
          9\t4\t7\t3
          3\t8\t6\t5
        `,
        expected: "9",
      }      
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
