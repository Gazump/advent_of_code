import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

enum Operator {
  PLUS = "+",
  MINUS = "-",
  TIMES = "*",
  DIVIDE = "/"
}

type Operation = {
  left: string;
  operator: Operator;
  right: string;
}

type Monkey = {  
  startingItems: number[];
  operation: Operation;
  divisibleBy: number;
  testPass: number;
  testFail: number;
  inspections: number;
}

const getOperation = (str: string): Operation => {  
  const operator = 
    str.includes(Operator.PLUS) ? Operator.PLUS : 
    str.includes(Operator.MINUS) ? Operator.MINUS :
    str.includes(Operator.TIMES) ? Operator.TIMES : Operator.DIVIDE;    
  const parts = str.slice(str.indexOf("=") + 2).split(operator);
  return {left: parts[0], operator: operator, right: parts[1]};
}

const doOperation = (value: number, operation: Operation): number => {
  const left: number = operation.left.includes("old") ? value : parseInt(operation.left);
  const right: number = operation.right.includes("old") ? value : parseInt(operation.right);  
  if ( operation.operator === Operator.PLUS )
    return left + right;
  if ( operation.operator === Operator.MINUS )
    return left - right;
  if ( operation.operator === Operator.TIMES )
    return left * right;
  if ( operation.operator === Operator.DIVIDE )
    return left / right;
  return -1;
}

const monkeyTurn = (monkey: Monkey, monkeys: Map<number, Monkey>, stressed = false, lcd?: number): void => {
  while (monkey.startingItems.length > 0) {
    monkey.inspections++;
    let worry = monkey.startingItems.shift()!;    
    worry = doOperation(worry, monkey.operation);    
    if (!stressed ) {
      worry = Math.floor(worry / 3);
    } else if (worry > lcd! ) {      
      worry -= (lcd! * (Math.floor(worry / lcd!) - 1));
    }    
    const throwTo = worry % monkey.divisibleBy === 0 ? monkey.testPass : monkey.testFail;
    monkeys.get(throwTo)?.startingItems.push(worry);
  }
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const monkeys: Map<number, Monkey> = new Map();

  for( let i = 0 ; i < input.length ; i+=7 ) {
    const startingItems = input[i + 1].slice(input[i + 1].indexOf(":") + 2).split(",").map(value => parseInt(value));
    const operation = getOperation(input[i + 2]);
    const divisibleBy = parseInt(input[i + 3].slice(input[i + 3].indexOf("y") + 2));
    const testPass = parseInt(input[i + 4].slice(input[i + 4].indexOf("y") + 2));
    const testFail = parseInt(input[i + 5].slice(input[i + 5].indexOf("y") + 2));

    monkeys.set(i/7, {startingItems, operation, divisibleBy, testPass, testFail, inspections: 0});    
  }

  for( let round = 1 ; round <= 20; round++ ) {
    for( let i = 0 ; i < monkeys.size; i++ ) {
      monkeyTurn(monkeys.get(i)!, monkeys);
    }    
  }

  let highest = 0;
  let second = 0;

  for( let i = 0 ; i < monkeys.size; i++ ) {
    const inspections = monkeys.get(i)!.inspections!;
    if (inspections > highest) {
      second = highest;
      highest = inspections;
    }
  }

  return (second * highest).toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const monkeys: Map<number, Monkey> = new Map();
  let lcd = 1;

  for( let i = 0 ; i < input.length ; i+=7 ) {
    const startingItems = input[i + 1].slice(input[i + 1].indexOf(":") + 2).split(",").map(value => parseInt(value));
    const operation = getOperation(input[i + 2]);
    const divisibleBy = parseInt(input[i + 3].slice(input[i + 3].indexOf("y") + 2));
    lcd *= divisibleBy;
    const testPass = parseInt(input[i + 4].slice(input[i + 4].indexOf("y") + 2));
    const testFail = parseInt(input[i + 5].slice(input[i + 5].indexOf("y") + 2));

    monkeys.set(i/7, {startingItems, operation, divisibleBy, testPass, testFail, inspections: 0});    
  }

  for( let round = 1 ; round <= 10000; round++ ) {
    for( let i = 0 ; i < monkeys.size; i++ ) {
      monkeyTurn(monkeys.get(i)!, monkeys, true, lcd);
    }    
  }

  let highest = 0;
  let second = 0;

  for( let i = 0 ; i < monkeys.size; i++ ) {
    const inspections = monkeys.get(i)!.inspections!;    
    if (inspections > highest) {      
      second = highest;
      highest = inspections;
    } else if (inspections > second) {
      second = inspections;
    }
  }

  return (second * highest).toString();
};

run({
  part1: {
    tests: [
      {
        input: `
          Monkey 0:
          Starting items: 79, 98
          Operation: new = old * 19
          Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
        
          Monkey 1:
            Starting items: 54, 65, 75, 74
            Operation: new = old + 6
            Test: divisible by 19
              If true: throw to monkey 2
              If false: throw to monkey 0
          
          Monkey 2:
            Starting items: 79, 60, 97
            Operation: new = old * old
            Test: divisible by 13
              If true: throw to monkey 1
              If false: throw to monkey 3
          
          Monkey 3:
            Starting items: 74
            Operation: new = old + 3
            Test: divisible by 17
              If true: throw to monkey 0
              If false: throw to monkey 1
        `,
        expected: "10605",
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
          Monkey 0:
          Starting items: 79, 98
          Operation: new = old * 19
          Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
        
          Monkey 1:
            Starting items: 54, 65, 75, 74
            Operation: new = old + 6
            Test: divisible by 19
              If true: throw to monkey 2
              If false: throw to monkey 0
          
          Monkey 2:
            Starting items: 79, 60, 97
            Operation: new = old * old
            Test: divisible by 13
              If true: throw to monkey 1
              If false: throw to monkey 3
          
          Monkey 3:
            Starting items: 74
            Operation: new = old + 3
            Test: divisible by 17
              If true: throw to monkey 0
              If false: throw to monkey 1
        `,
        expected: "2713310158",
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
