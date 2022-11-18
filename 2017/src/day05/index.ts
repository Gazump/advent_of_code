import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n").map((string) => parseInt(string));
  let i = 0;
  let steps = 0;

  while (i >= 0 && i < input.length) {    
    const here = i;
    i += input[i];
    input[here]++;
    steps++;    
  }
  return steps.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n").map((string) => parseInt(string));
  let i = 0;
  let steps = 0;

  while (i >= 0 && i < input.length) {    
    const here = i;
    i += input[i];
    input[here] >= 3 ? input[here]-- : input[here]++
    steps++;    
  }
  return steps.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
        0
        3
        0
        1
        -3
        `,
        expected: "5",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
        0
        3
        0
        1
        -3
        `,
        expected: "10",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
