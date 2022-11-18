import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");

  let count = 0;
  input.forEach((line) => {
    const keys = line.split(" ");
    const duplicates = keys.filter((key, index) => keys.indexOf(key) !== index);
    count += duplicates.length > 0 ? 0 : 1;
  });

  return count;
};

const part2 = (rawInput: string) => {  
  const input = parseInput(rawInput).split("\n");

  let count = 0;
  input.forEach((line) => {
    const keys = line.split(" ").map((key) => key.split("").sort().join());
    const duplicates = keys.filter((key, index) => keys.indexOf(key) !== index);
    count += duplicates.length > 0 ? 0 : 1;
  });

  return count;
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
      // {
      //   input: ``,
      //   expected: "",
      // },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
