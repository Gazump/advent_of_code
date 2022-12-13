import run from "aocrunner";
import { start } from "repl";

const parseInput = (rawInput: string) => rawInput;

type Point = {
  x: number;
  y: number;
}

const pointToString = (point: Point): string => {
  return `${point.x}_${point.y}`;
}

const stringToPoint = (string: string): Point => {
  const parts = string.split("_");
  return {x: parseInt(parts[0]), y: parseInt(parts[1])};
}

const charToHeight = (char: string): number => {
  if (char === "S")
    return 1;
  else if (char === "E")
    return 26;
  else 
    return char.charCodeAt(0) - 96;
}

const findPossibleAdjacents = (point: Point, grid: string[][]): string[] => {
  const thisHeight = charToHeight(grid[point.y][point.x]);
  const possibleAdjacents: string[] = [];
  
  [{x: 0, y: 1}, {x:1, y: 0}, {x:0, y: -1}, {x:-1, y: 0}].forEach(adj => {
      if (!(adj.x === 0 && adj.y === 0)) {
        const adjacent = {x: point.x + adj.x, y: point.y + adj.y};
        if(adjacent.x >= 0 && adjacent.x < grid[0].length && adjacent.y >= 0 && adjacent.y < grid.length ) {          
          if( charToHeight(grid[adjacent.y][adjacent.x]) - thisHeight <= 1) {
            possibleAdjacents.push(pointToString({x: point.x + adj.x, y: point.y + adj.y}));
          }
        }        
      }
  });

  return possibleAdjacents;
}

const updateChildrenPathCost = (parentKey: string, nodes: Map<string, string[]>, costMap: Map<string, number>): void => {
  nodes.get(parentKey)!.forEach((adjacent) => {
    const thisCost = costMap.get(parentKey)!;
    if( thisCost + 1 < costMap.get(adjacent)!) {        
      costMap.set(adjacent, thisCost + 1);
      updateChildrenPathCost(adjacent, nodes, costMap);
    }
  });
}

const findShortestPath = (start: Point, end: Point, nodes: Map<string, string[]>, costMap: Map<string, number>): void => {  
  nodes.get(pointToString(start))!.forEach((adjacent) => {
    const startCost = costMap.get(pointToString(start))!;
    
    if (costMap.has(adjacent)) {
      const adjCost = costMap.get(adjacent)!;
      if( startCost + 1 < adjCost) {        
        costMap.set(adjacent, startCost + 1);
        updateChildrenPathCost(adjacent, nodes, costMap);
      }
    } else {
      costMap.set(adjacent, startCost + 1);
      findShortestPath(stringToPoint(adjacent), end, nodes, costMap);
    }
  });
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const grid: string[][] = new Array();

  input.forEach((line) => {
    const chars = line.split("");
    grid.push(chars);
  });

  const nodes: Map<string, string[]> = new Map();
  let start: Point;
  let end: Point;

  for( let y = 0 ; y < grid.length ; y++) {
    for( let x = 0 ; x < grid[0].length ; x++) {    
      const key = pointToString({x, y});

      nodes.set(key, findPossibleAdjacents({x, y}, grid));
      if (grid[y][x] === "S") {
        start = {x, y};
      } else if (grid[y][x] === "E") {
        end = {x, y};
      }
    }
  }

  const costMap: Map<string, number> = new Map();
  costMap.set(pointToString(start!), 0);

  findShortestPath(start!, end!, nodes, costMap);

  return costMap.get(pointToString(end!))!.toString();
};

const part2 = (rawInput: string) => {  
  const input = parseInput(rawInput).split("\n");
  const grid: string[][] = new Array();

  input.forEach((line) => {
    const chars = line.split("");
    grid.push(chars);
  });

  const starts = [];

  const nodes: Map<string, string[]> = new Map();  
  let end: Point;

  for( let y = 0 ; y < grid.length ; y++) {
    for( let x = 0 ; x < grid[0].length ; x++) {    
      const key = pointToString({x, y});

      nodes.set(key, findPossibleAdjacents({x, y}, grid));
      if (grid[y][x] === "S" || grid[y][x] === "a" ) {        
        starts.push({x, y});
      } else if (grid[y][x] === "E") {
        end = {x, y};
      }
    }
  }

  let shortest = 99999999;

  // brute-force on all a's. Could cut this down a lot by
  // checking if any a's are on the correct path and then
  // just subtracting for those
  starts.forEach(start => {
    const costMap: Map<string, number> = new Map();
    costMap.set(pointToString(start!), 0);

    findShortestPath(start!, end!, nodes, costMap);

    const cost = costMap.get(pointToString(end!))!;
    if (cost < shortest) {
      shortest = cost;
    }
  });

  return shortest.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          Sabqponm
          abcryxxl
          accszExk
          acctuvwj
          abdefghi
        `,
        expected: "31",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          Sabqponm
          abcryxxl
          accszExk
          acctuvwj
          abdefghi
        `,
        expected: "29",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
