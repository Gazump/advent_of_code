import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const getCommonCharacter = (a: string, b: string, c?: string): string | undefined => {
  return Array.from(a).find((char) => {
    return c && b.includes(char) ? c.includes(char) : b.includes(char);
  });
}

const getPriority = (char: string): number => {  
  const code = char.charCodeAt(0);
  return  code >= 97 ? code - 96 : code - 38;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  let sum = 0;

  input.forEach((line) => {
    const compartments = { one:line.slice(0, line.length / 2), two: line.slice(line.length / 2)};    
    const error = getCommonCharacter(compartments.one, compartments.two);    
    const priority = getPriority(error!);    
    sum += priority;    
  });

  return sum.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  let sum = 0;

  for (let i = 0; i < input.length; i += 3) {
    const rucksacks = { one: input[i], two: input[i+1], three: input[i+2] };
    const error = getCommonCharacter(rucksacks.one, rucksacks.two, rucksacks.three);
    sum += getPriority(error!);
  }
  
  return sum.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          vJrwpWtwJgWrhcsFMMfFFhFp
          jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
          PmmdzqPrVvPwwTWBwg
          wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
          ttgJtRGJQctTZtZT
          CrZsJsPPZsGzwwsLwLmpwMDw
        `,
        expected: "157",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          vJrwpWtwJgWrhcsFMMfFFhFp
          jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
          PmmdzqPrVvPwwTWBwg
          wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
          ttgJtRGJQctTZtZT
          CrZsJsPPZsGzwwsLwLmpwMDw
        `,
        expected: "70",
      },
      {
        input: `
          NGWdQgDDHGJgQLznzzsJFFzvzB
          twRCpZVjVWqVSqVwwjtZfrrfntfvznBssBncfLrc
          jRRwCqwCZhlhZRpSZpjSqWwqmDMQdMmHPQQMHGdlHdTldNGd
        `,
        expected: "49",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
