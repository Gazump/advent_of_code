import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

enum Direction {
  right,
  up,
  left,
  down
}

const part1 = (rawInput: string) => {
  const input = parseInt(parseInput(rawInput));

  let r = 0;
  let c = 0;

  let direction: number = Direction.right;

  const map: Map<number, {x: number, y: number}> = new Map();

  for (let i = 1; i <= input; i++) {
    map.set(i, {x: c, y: r});

    const sqrt = Math.floor(Math.sqrt(i)) + 1;

    switch(direction) {
      case Direction.right: {
        c++;        
        if(i == Math.pow(sqrt - 1, 2)) {
          direction = Direction.up;
        }
        break;
      };
      case Direction.up: {
        r--;
        if(i + sqrt == sqrt * sqrt) {
          direction = Direction.left;
        }
        break;
      };
      case Direction.left: {
        c--;
        if(i == Math.pow(sqrt - 1, 2)) {
          direction = Direction.down;
        }
        break;
      };
      case Direction.down: {
        r++;
        if(i + sqrt == sqrt * sqrt) {
          direction = Direction.right;
        }
        break;
      };
    }
  }

  const node = map.get(input);

  return node ? (Math.abs(node.x) + Math.abs(node.y)).toString() : undefined;
};

const part2 = (rawInput: string) => {
  const input = parseInt(parseInput(rawInput));

  let r = 0;
  let c = 1;

  let direction: number = Direction.up;

  const map: Map<string, number> = new Map();
  map.set("0_0", 1);  

  let i = 2;
  while( i < input) {
    // get possible adjacents
    let sum = 0;
    for (let x = -1; x <= 1 ; x++) {
      for (let y = -1; y <= 1 ; y++) {
        const point = {x: c + x, y: r + y};        
        if (!( x == 0 && y == 0) && map.has(`${point.x}_${point.y}`)) {
          sum += map.get(`${point.x}_${point.y}`)!;
        }
      
      }
    }    
    map.set(`${c}_${r}`, sum);
    if (sum > input) {
      return sum.toString();
    }

    const sqrt = Math.floor(Math.sqrt(i)) + 1;

    switch(direction) {
      case Direction.right: {
        c++;        
        if(i == Math.pow(sqrt - 1, 2)) {
          direction = Direction.up;
        }
        break;
      };
      case Direction.up: { 
        r--;
        if(i + sqrt == sqrt * sqrt) {
          direction = Direction.left;
        }
        break;
      };
      case Direction.left: {
        c--;
        if(i == Math.pow(sqrt - 1, 2)) {
          direction = Direction.down;
        }
        break;
      };
      case Direction.down: {
        r++;
        if(i + sqrt == sqrt * sqrt) {
          direction = Direction.right;
        }
        break;
      };
    }
    i++;
  }

  return;
};

run({
  part1: {
    tests: [
      {
        input: `1`,
        expected: "0",
      },
      {
        input: `12`,
        expected: "3",
      },
      {
        input: `23`,
        expected: "2",
      },
      {
        input: `1024`,
        expected: "31",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `100`,
        expected: "122",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
