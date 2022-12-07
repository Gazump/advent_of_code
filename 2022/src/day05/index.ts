import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

const formStacks = (line: string, stacks: Map<number, string[]>) => {
  for (let i = 1 ; i <= line.length / 4 + 1 ; i++) {
    const crate = line[1 + (i-1)*4];
    if( crate !== " ") {
      if(stacks.has(i) ) {
        stacks.get(i)?.unshift(crate);
      } else {
        stacks.set(i, [crate]);
      }
    }
  }
}

const getOutputCode = (stacks: Map<number, string[]>): string => {
  let output = "";
  for(let i = 1 ; i <= stacks.size ; i++) {
    output += stacks.get(i)?.pop();
  }
  return output;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const stacks: Map<number, string[]> = new Map();

  input.forEach((line) => {
    if(line.length > 0) {
      if(line.slice(0, 4) === "move") {
        const parts = line.split(" ");
        const count = parseInt(parts[1]);
        const from = parseInt(parts[3]);
        const to = parseInt(parts[5]);

        for(let i = 0 ; i < count ; i++) {
          stacks.get(to)?.push(stacks.get(from)?.pop()!);
        }        
      } else if(line.includes("[")) {
        formStacks(line, stacks);
      }
    }
  }); 

  return getOutputCode(stacks);
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const stacks: Map<number, string[]> = new Map();

  input.forEach((line) => {
    if(line.length > 0) {
      if(line.slice(0, 4) === "move") {
        const parts = line.split(" ");
        const count = parseInt(parts[1]);
        const from = parseInt(parts[3]);
        const to = parseInt(parts[5]);
        const newStacks = [];

        for(let i = 0 ; i < count ; i++) {
          newStacks.unshift(stacks.get(from)?.pop()!);
        }
        newStacks.forEach((stack) => {
          stacks.get(to)?.push(stack);
        });
      } else if(line.includes("[")) {
        formStacks(line, stacks);
      }
    }
  });

  return getOutputCode(stacks);
};

run({
  part1: {
    tests: [
      {
        input: `
          [ ] [D]
          [N] [C]    
          [Z] [M] [P]
           1   2   3 
          
          move 1 from 2 to 1
          move 3 from 1 to 3
          move 2 from 2 to 1
          move 1 from 1 to 2
        `,
        expected: "CMZ",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          [ ] [D]
          [N] [C]    
          [Z] [M] [P]
           1   2   3 
          
          move 1 from 2 to 1
          move 3 from 1 to 3
          move 2 from 2 to 1
          move 1 from 1 to 2
        `,
        expected: "MCD",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
