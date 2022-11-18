import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const part1 = (rawInput: string) => {
  let input = parseInput(rawInput);

  return input.split("").filter( (char: string, i: number) => char === input[(i+1) % input.length]).map((char) => parseInt(char)).reduce((acc: number, val: number) => acc + val, 0).toString();  
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);

  return input.split("").filter( (char: string, i: number) => char === input[(i+input.length/2) % input.length]).map((char) => parseInt(char)).reduce((acc: number, val: number) => acc + val, 0).toString();
};

run({
  part1: {
    tests: [
      {
        input: `1122`,
        expected: "3",
      },
      {
        input: `1111`,
        expected: "4",
      },
      {
        input: `1234`,
        expected: "0",
      },
      {
        input: `91212129`,
        expected: "9",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `1212`,
        expected: "6",
      },
      {
        input: `1221`,
        expected: "0",
      },
      {
        input: `123425`,
        expected: "4",
      },
      {
        input: `123123`,
        expected: "12",
      },
      {
        input: `12131415`,
        expected: "4",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
