import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  let count = 0;

  input.forEach((line) => {
    const parts = line.split(",");
    const elf1 = parts[0].split("-").map((char) => { return parseInt(char)});
    const elf2 = parts[1].split("-").map((char) => { return parseInt(char)});;

    if ( (elf1[0] <= elf2[0] && elf1[1] >= elf2[1]) || (elf2[0] <= elf1[0] && elf2[1] >= elf1[1]) ) {
      count++;
    }
  });  

  return count.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  let count = 0;

  input.forEach((line) => {
    const parts = line.split(",");
    const elf1 = parts[0].split("-").map((char) => { return parseInt(char)});
    const elf2 = parts[1].split("-").map((char) => { return parseInt(char)});;

    if ( (elf1[0] >= elf2[0] && elf1[0] <= elf2[1]) || (elf2[0] >= elf1[0] && elf2[0] <= elf1[1])  ) {
      count++;
    }
  });  

  return count.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          2-4,6-8
          2-3,4-5
          5-7,7-9
          2-8,3-7
          2-6,4-6
          2-6,4-8
        `,
        expected: "2",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          2-4,6-8
          2-3,4-5
          5-7,7-9
          2-8,3-7
          2-6,4-6
          2-6,4-8
        `,
        expected: "4",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
