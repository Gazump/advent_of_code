import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

enum Move {
  ROCK = 1,
  PAPER = 2,
  SCISSORS = 3
}

enum Result {  
  LOSS = 0,
  DRAW = 3,
  WIN = 6
}

const movesMap: Map<string, Move> = new Map();
movesMap.set("A", Move.ROCK);
movesMap.set("B", Move.PAPER);
movesMap.set("C", Move.SCISSORS);
movesMap.set("X", Move.ROCK);
movesMap.set("Y", Move.PAPER);
movesMap.set("Z", Move.SCISSORS);

const resultMap: Map<string, Result> = new Map();
resultMap.set("X", Result.LOSS);
resultMap.set("Y", Result.DRAW);
resultMap.set("Z", Result.WIN);

const checkWin = (move1: Move, move2: Move): Result => {
  if(move1 === move2) 
    return Result.DRAW;  
  if ((move1 === Move.ROCK && move2 === Move.SCISSORS) ||
      (move1 === Move.PAPER && move2 === Move.ROCK) ||
      (move1 === Move.SCISSORS && move2 === Move.PAPER))
    return Result.WIN;
  return Result.LOSS;
}

const checkStrategy = (move1: Move, result: Result): Move => {
  if( result === Result.WIN) {
    if (move1 === Move.ROCK) return Move.PAPER;
    if (move1 === Move.PAPER) return Move.SCISSORS;
    if (move1 === Move.SCISSORS) return Move.ROCK;      
  }
  if( result === Result.LOSS) {
    if (move1 === Move.ROCK) return Move.SCISSORS;
    if (move1 === Move.PAPER) return Move.ROCK;
    if (move1 === Move.SCISSORS) return Move.PAPER;      
  }
  return move1;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");

  let score = 0;

  input.forEach((line) => {
    const plays = line.split(" ");
    const opponent = movesMap.get(plays[0]);
    const you = movesMap.get(plays[1]);

    score += you! + checkWin(you!, opponent!);
  });

  return score.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");

  let score = 0;

  input.forEach((line) => {
    const plays = line.split(" ");
    const opponent = movesMap.get(plays[0]);
    const result = resultMap.get(plays[1]);
    
    const you = checkStrategy(opponent!, result!);
    score += you! + checkWin(you!, opponent!);
  });

  return score.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          A Y
          B X
          C Z
        `,
        expected: "15",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          A Y
          B X
          C Z
        `,
        expected: "12",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
