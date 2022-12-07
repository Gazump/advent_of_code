import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const checkForMarker = (characters: string[]): boolean => {
  return (new Set(characters)).size === characters.length;
}

const findMarker = (rawInput: string, size: number): number | undefined => {
  const input = Array.from(rawInput);
  for(let i = size + 1 ; i < input.length ; i++) {
    if (checkForMarker(input.slice(i-size+1, i+1))) {      
      return i + 1;
    }
  }
}

const part1 = (rawInput: string) => {
  return findMarker(rawInput, 4)!.toString();
};

const part2 = (rawInput: string) => {
  return findMarker(rawInput, 14)!.toString();
};

run({
  part1: {
    tests: [
      {
        input: `bvwbjplbgvbhsrlpgdmjqwftvncz`,
        expected: "5",
      },
      {
        input: `nppdvjthqldpwncqszvftbrmjlhg`,
        expected: "6",
      },
      {
        input: `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`,
        expected: "10",
      },
      {
        input: `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`,
        expected: "11",
      },
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
