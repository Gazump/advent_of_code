import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

type Tree = {
  height: number;
  visible: boolean;
}

const linesToGrid = (lines: string[]): Tree[][] => {
  const grid = new Array();
  lines.forEach((line, rowIndex) => {
    const row = line.split("").map((char, colIndex) => {return {height: parseInt(char), visible: colIndex === 0 || colIndex === line.length - 1 || rowIndex === 0 || rowIndex === grid.length - 1 }});
    grid.push(row);
  });
  return grid;
}

const countVisibleTrees = (array: Tree[]): number => {
  let count = 0;
  let tallest = array[0].height;

  for (let i = 1 ; i < array.length - 1 ; i++) {
    if ( array[i].height > tallest) { 
      tallest = array[i].height;
      if (!array[i].visible ) {          
        count++;      
        array[i].visible = true;
      }
    }
  }
  return count;
}

const calculateScene = (grid: Tree[][], row: number, col: number): number => {
  const here = grid[row][col].height;  
  let sceneScore = 1;

  //left
  let count = 0;
  for( let c = col - 1 ; c >= 0 ; c--) {
    count++;      
    if (grid[row][c].height >= here )
      break;
  }
  sceneScore *= count;

  // right
  count = 0;
  for( let c = col + 1 ; c < grid[0].length ; c++) {    
    count++;      
    if (grid[row][c].height >= here ) 
      break;
  }
  sceneScore *= count;

  //up
  count = 0;
  for( let r = row - 1 ; r >= 0 ; r--) {    
    count++;      
    if (grid[r][col].height >= here )      
      break;
  }
  sceneScore *= count;

  // down
  count = 0;
  for( let r = row + 1 ; r < grid.length ; r++) {    
    count++;      
    if (grid[r][col].height >= here )      
      break;
  }
  sceneScore *= count;

  return sceneScore;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const grid = linesToGrid(input);  
  let count = grid.length * 2 + grid[0].length * 2 - 4;

  for (let row = 1 ; row < grid.length - 1 ; row++) {    
    count += countVisibleTrees(grid[row]);
    count += countVisibleTrees(grid[row].slice().reverse());
      
  }  
  for (let col = 1 ; col < grid[0].length - 1 ; col++) {
    const column = grid.map((row) => { return row[col] });   
    count += countVisibleTrees(column);
    count += countVisibleTrees(column.slice().reverse());   
  }  

  return count.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const grid = linesToGrid(input);

  let bestScene = 0;

  for ( let row = 0; row < grid.length ; row++) {
    for ( let col = 0; col < grid[0].length ; col++) {
      const scene = calculateScene(grid, row, col);
      if (scene > bestScene) {
        bestScene = scene;
      }
    }
  }

  return bestScene.toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          30373
          25512
          65332
          33549
          35390
        `,
        expected: "21",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          30373
          25512
          65332
          33549
          35390
        `,
        expected: "8",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
