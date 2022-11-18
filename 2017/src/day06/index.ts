import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input: number[] = parseInput(rawInput).split("\t").map((string) => parseInt(string));
  const map: Map<string, boolean> = new Map();

  let steps = 0;
  while (!map.has(input.toString())) {
    map.set(input.toString(), true);
    let i = input.findIndex((num) => num === Math.max(...input));
    let c = input[i];
    input[i] = 0;

    while (c > 0) {
      if (++i >= input.length) {
        i = 0;
      }
      input[i]++;
      c--;
    }    
    steps++;
  }
  return steps.toString();
};

const part2 = (rawInput: string) => {
  const input: number[] = parseInput(rawInput).split("\t").map((string) => parseInt(string));
  const map: Map<string, number> = new Map();
  let steps = 0;

  while (!map.has(input.toString())) {
    map.set(input.toString(), steps);
    let i = input.findIndex((num) => num === Math.max(...input));
    let c = input[i];
    input[i] = 0;

    while (c > 0) {
      if (++i >= input.length) {
        i = 0;
      }
      input[i]++;
      c--;
    }    
    steps++;
  }
  return (steps - map.get(input.toString())!).toString();
};

run({
  part1: {
    tests: [
      {
        input: `0\t2\t7\t0`,
        expected: "5",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `0\t2\t7\t0`,
        expected: "4",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
