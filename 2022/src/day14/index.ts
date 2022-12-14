import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

enum Type {
  Space = ".",
  Rock = "#",
  Sand = "o"
}

type Point = {
  x: number;
  y: number;
}

const stringToPoint = (str: string): Point => {
  const parts = str.split(",");
  return {x: parseInt(parts[0]), y: parseInt(parts[1])};
}

const pointToString = (point: Point): string => {
  return `${point.x},${point.y}`;
}

const setToType = (map: Map<string, Type>, x: number, y: number, type: Type, isBedRock = false) => {
  map.set(pointToString({x: x, y: y}), type);
  if (!isBedRock) {
    if (y > bedRock.y) 
      bedRock.y = y;
    if (x > bedRock.maxX) 
      bedRock.maxX = x;
    if (x < bedRock.minX)
      bedRock.minX = x;
  }
}

const createRocks = (map: Map<string, Type>, from: Point, to: Point, isBedRock = false): void => {
  let x = from.x;
  let y = from.y;
  while (x !== to.x || y !== to.y) {
    setToType(map, x, y, Type.Rock, isBedRock);
    x += (to.x - from.x) / Math.abs(to.x - from.x) || 0;
    y += (to.y - from.y) / Math.abs(to.y - from.y) || 0;
  }
  setToType(map, x, y, Type.Rock, isBedRock);
}

const dropSand = (map: Map<string, Type>, isVoid = true): boolean => {
  let x = 500;
  let y = 0;
  let settled = false;

  while(!settled) {
    if ( isVoid && y + 1 > bedRock.y) {
        return false;
    }    
    if (!map.has(pointToString({x: x, y: y + 1}))) {
      y++;
    } else if(!map.has(pointToString({x: x - 1, y: y + 1}))) {
      x--;
      y++;
    } else if(!map.has(pointToString({x: x + 1, y: y + 1}))) {
      x++;
      y++;
    } else {
      settled = true;
      map.set(pointToString({x: x, y: y}), Type.Sand);
      if (!isVoid && x === 500 && y === 0) {
        return false;
      }
    }
  }
  return true;
}

let bedRock: {minX: number, maxX: number, y: number};

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const map: Map<string, Type> = new Map();
  bedRock = {minX: 0, maxX: 0, y: 0};

  input.forEach((line) => {
    const points = line.split(" -> ");    
    let from = stringToPoint(points[0]);

    for (let i = 1; i < points.length ; i++) {
      const to = stringToPoint(points[i]);
      createRocks(map, from, to);
      from = stringToPoint(points[i]);
    }
  });

  let count = 0;
  while(dropSand(map)) {
    count++;
  }

  return count.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const map: Map<string, Type> = new Map();
  bedRock = {minX: 0, maxX: 0, y: 0};

  input.forEach((line) => {
    const points = line.split(" -> ");    
    let from = stringToPoint(points[0]);
    
    for (let i = 1; i < points.length ; i++) {
      const to = stringToPoint(points[i]);
      createRocks(map, from, to);
      from = stringToPoint(points[i]);
    }
  });

  createRocks(map, {x: bedRock.minX - 500, y: bedRock.y + 2}, {x: bedRock.maxX + 500, y: bedRock.y + 2}, true);

  let count = 0;
  while(dropSand(map, false)) {
    count++;
  }
  count++;

  return count.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          498,4 -> 498,6 -> 496,6
          503,4 -> 502,4 -> 502,9 -> 494,9
        `,
        expected: "24",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          498,4 -> 498,6 -> 496,6
          503,4 -> 502,4 -> 502,9 -> 494,9
        `,
        expected: "93",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
