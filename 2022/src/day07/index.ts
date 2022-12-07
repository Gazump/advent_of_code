import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

type File = {
  name: string;
  size: number;
}

type Directory = {
  name: string;
  parent: Directory | undefined;
  subs: Map<string, Directory>;
  files: File[];
  size: number;
}

const command = (parameters: string[]): void => { 
  const instruction = parameters[0]; 
  if (instruction === "ls") {
    outputting = true;
  } else if (instruction == "cd") {
    if(parameters[1] === "..") {
      currentDir = currentDir.parent!;
    } else if (parameters[1] === "/") {
      currentDir = fileSystem.get(parameters[1])!;
    } else {      
      currentDir = currentDir.subs.get(parameters[1])!;
    }    
  }
}

const ls = (parameters: string[]): void => {  
  if( parameters[0] === "dir" ) {    
    const newDirName = parameters[1];
    if (!fileSystem.has(newDirName)) {
      const newDir: Directory = {name: newDirName, parent: currentDir, files: [], subs: new Map(), size: 0};
      fileSystem.set(newDirName, newDir);
      currentDir.subs.set(newDirName, newDir);
    } else {
      // duplicate directory name
      const newDir: Directory = {name: newDirName, parent: currentDir, files: [], subs: new Map(), size: 0};
      fileSystem.set(`${newDirName}_${duplicates++}`, newDir);
      currentDir.subs.set(newDirName, newDir);
    }
  } else {
    // must be a file
    const newFile: File = { name: parameters[1], size: parseInt(parameters[0]) };
    currentDir.files.push(newFile);
    updateDirectorySize(currentDir, newFile.size);
  }
}

const updateDirectorySize = (directory: Directory, amount: number): void => {
  directory.size += amount;
  if( directory.parent !== undefined) {
    updateDirectorySize(directory.parent, amount);
  }
}

const buildFileSystem = (input: string[]) => {
  fileSystem = new Map();
  outputting = false;  
  duplicates = 0;
  fileSystem.set("/", {name: "/", parent: undefined, subs: new Map(), files: [], size: 0});
  currentDir = fileSystem.get("/")!;

  input.forEach((line) => {
    const parts = line.split(" ");
    if (parts[0] === "$") {
      outputting = false;
      command(parts.slice(1));
    } else if( outputting ) {
      ls(parts);
    }
  });
}

let fileSystem: Map<string, Directory>;
let outputting: boolean;
let currentDir: Directory;
let duplicates: number;

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  buildFileSystem(input);
  let output = 0;

  for (let [key, value] of fileSystem) {
    if (value.size <= 100000) {
      output += value.size;
    }
  }

  return output.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  buildFileSystem(input);  
  const outer = fileSystem.get("/")?.size;
  let smallest = outer!;

  for (let value of fileSystem.values()) {
    if (70000000 - outer! + value.size >= 30000000 && value.size < smallest) {
      smallest = value.size;
    }
  }

  return smallest.toString();
};

run({
  part1: {
    tests: [
      // {
      //   input: ``,
      //   expected: "",
      // },
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
