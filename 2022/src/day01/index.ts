import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");

  const elves: number[] = [];
  let elf = 0;
  let counter = 0;

  input.forEach((line) => {
    if(line == "") {
      elves[elf] = counter;
      counter = 0;
      elf++;
    } else {
      counter += parseInt(line);
    }
  });

  elves[elf] = counter;

  return Math.max(...elves).toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const elves: number[] = [];
  let elf = 0;
  let counter = 0;

  input.forEach((line) => {
    if(line == "") {
      elves[elf] = counter;
      counter = 0;
      elf++;
    } else {
      counter += parseInt(line);
    }
  });

  elves[elf] = counter;

  const sorted = elves.sort((a, b) => b - a);

  return sorted.slice(0, 3).reduce((acc, val) => { return acc + val }, 0).toString();
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
          1000
          2000
          3000

          4000

          5000
          6000

          7000
          8000
          9000

          10000
        `,
        expected: "45000",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
