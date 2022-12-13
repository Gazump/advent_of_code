import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

type Point = {
  x: number,
  y: number
}

enum Direction {
  UP = "U",
  DOWN = "D",
  LEFT = "L",
  RIGHT = "R" 
}

const pointToString = (point: Point): string => {
  return `${point.x}_${point.y}`;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");  
  const head: Point = {x: 0, y: 0};
  const tail: Point = {x: 0, y: 0};
  const positions: Set<string> = new Set([pointToString(tail)]);

  input.forEach((line) => {
    const parts = line.split(" ");
    const direction = parts[0];
    const distance = parseInt(parts[1]);

    for (let i = 0 ; i < distance ; i++) {      
      moveHead(head, direction);
      follow(tail, head);
      positions.add(pointToString(tail));
    }
  });

  return positions.size.toString();
};

const moveHead = (head: Point, direction: string): void => {
  if(direction === Direction.LEFT)
    head.x--;
  else if(direction === Direction.RIGHT)
    head.x++;
  else if(direction === Direction.UP)
    head.y--;
  else if(direction === Direction.DOWN)
    head.y++;
}

const follow = (knot: Point, previousKnot: Point): void => {
  while (Math.abs(knot.x - previousKnot.x) > 1 || Math.abs(knot.y - previousKnot.y) > 1) {
    if (Math.abs(knot.x - previousKnot.x) > 0 && Math.abs(knot.y - previousKnot.y) > 0 ) {
      knot.x += (previousKnot.x - knot.x) / Math.abs(knot.x - previousKnot.x);
      knot.y += (previousKnot.y - knot.y) / Math.abs(knot.y - previousKnot.y);
    }
    else if (Math.abs(knot.x - previousKnot.x) > 1) {      
      knot.x += (previousKnot.x - knot.x) / Math.abs(knot.x - previousKnot.x);
    }
    else if (Math.abs(knot.y - previousKnot.y) > 1) {    
      knot.y += (previousKnot.y - knot.y) / Math.abs(knot.y - previousKnot.y);
    }
  }
}

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");  
  const knots: Point[] = [];
  for (let i = 0 ; i < 10 ; i++) {
    knots.push({x: 0, y: 0});
  }
  const positions: Set<string> = new Set([pointToString(knots[9])]);

  input.forEach((line) => {
    const parts = line.split(" ");
    const direction = parts[0];
    const distance = parseInt(parts[1]);

    for (let i = 0 ; i < distance ; i++) {      
      moveHead(knots[0], direction);
      for(let k = 1 ; k < 10 ; k++) {        
        follow(knots[k], knots[k-1]);
      }      
      positions.add(pointToString(knots[9]));
    }
  }); 

  return positions.size.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          R 4
          U 4
          L 3
          D 1
          R 4
          D 1
          L 5
          R 2
        `,
        expected: "13",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          R 4
          U 4
          L 3
          D 1
          R 4
          D 1
          L 5
          R 2
        `,
        expected: "1",
      },
      {
        input: `
          R 5
          U 8
          L 8
          D 3
          R 17
          D 10
          L 25
          U 20
        `,
        expected: "36",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
