import run from "aocrunner";

const parseInput = (rawInput: string) => rawInput;

type Point = {
  x: number;
  y: number;
}

enum Type {
  BEACON = "B",
  SENSOR = "S",
  EMPTY = "#",
  UNSCANNED = "."
}

const pointToString = (point: Point): string => {
  return `${point.x},${point.y}`;
}

const getManhattanDistance = (from: Point, to: Point): number => {
  return Math.abs(from.x - to.x) + Math.abs(from.y - to.y);
}

type Range = {
  from: number;
  to: number;
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");

  const map: Map<string, string> = new Map();
  let minX = 0;
  let maxX = 0;

  input.forEach((line) => {
    const parts = line.split(":");
    const sensor: Point = {x: parseInt(parts[0].slice(parts[0].indexOf("=") + 1, parts[0].indexOf(","))), y: parseInt(parts[0].slice(parts[0].indexOf("=", parts[0].indexOf("=") + 1) + 1))};
    const beacon: Point = {x: parseInt(parts[1].slice(parts[1].indexOf("=") + 1, parts[1].indexOf(","))), y: parseInt(parts[1].slice(parts[1].indexOf("=", parts[1].indexOf("=") + 1) + 1))};        
    const distance = getManhattanDistance(sensor, beacon);    

    map.set(pointToString(sensor), Type.SENSOR);
    map.set(pointToString(beacon), Type.BEACON);
    
    if (sensor.y - distance <= 2000000 && sensor.y + distance >= 2000000) {
      for ( let y = sensor.y - distance ; y <= sensor.y + distance ; y++ ) {
        if ( y === 2000000 ) {
          const xShift = distance - Math.abs(sensor.y - y);
          for ( let x = sensor.x - xShift ; x <= sensor.x + xShift; x++ ) {
            const pointKey = pointToString({x, y});
            if (!map.has(pointKey)) {
              map.set(pointKey, Type.EMPTY);
            }
            if (x < minX) 
              minX = x;
            if (x > maxX) 
              maxX = x;
          }
        }      
      }
    }
    
  });

  let count = 0;

  for ( let x = minX ; x <= maxX; x++ ) {
    const pointKey = pointToString({x, y: 2000000});
    if(map.has(pointKey)) {
      if(map.get(pointKey) === Type.EMPTY) {
        count++;
      }
    }
  }

  return count.toString();
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput).split("\n");
  const map: Map<number, Range[]> = new Map();

  const limit = 4000000;

  input.forEach((line) => {
    const parts = line.split(":");
    const sensor: Point = {x: parseInt(parts[0].slice(parts[0].indexOf("=") + 1, parts[0].indexOf(","))), y: parseInt(parts[0].slice(parts[0].indexOf("=", parts[0].indexOf("=") + 1) + 1))};
    const beacon: Point = {x: parseInt(parts[1].slice(parts[1].indexOf("=") + 1, parts[1].indexOf(","))), y: parseInt(parts[1].slice(parts[1].indexOf("=", parts[1].indexOf("=") + 1) + 1))};        
    const distance = getManhattanDistance(sensor, beacon);
    
    for ( let y = sensor.y - distance ; y <= sensor.y + distance ; y++ ) {
      const xShift = distance - Math.abs(sensor.y - y);
      const from = sensor.x - xShift;
      const to = sensor.x + xShift;

      if (map.has(y)) {
        map.get(y)!.push({from, to});
      } else {
        map.set(y, [{from, to}]);
      }
      
    }
  });

  for ( let y = 0 ; y <= limit ; y++ ) {
    let ranges = map.get(y)!;

    ranges.sort((a, b) => {
      return a.from < b.from ? -1 : a.from > b.from ? 1 : 0;
    });

    ranges = ranges.map((range) => {
      return {from: Math.max(range.from, 0), to: Math.min(range.to, limit)}
    });

    for ( let i = 1 ; i < ranges.length ; i++) {
      if (ranges[i-1].to > ranges[i].from) {
        ranges[i].from = ranges[i-1].to;
        if (ranges[i].from > ranges[i].to) {
          ranges[i].to = ranges[i].from;
        }
      }
    }

    for ( let i = 1 ; i < ranges.length ; i++) {
      if (ranges[i-1].to + 1 < ranges[i].from) {
        return ((ranges[i-1].to + 1) * 4000000 + y).toString();
      }
    }
  }

  return "";
};

run({
  part1: {
    tests: [
      // {
      //   input: `
      //     Sensor at x=2, y=18: closest beacon is at x=-2, y=15
      //     Sensor at x=9, y=16: closest beacon is at x=10, y=16
      //     Sensor at x=13, y=2: closest beacon is at x=15, y=3
      //     Sensor at x=12, y=14: closest beacon is at x=10, y=16
      //     Sensor at x=10, y=20: closest beacon is at x=10, y=16
      //     Sensor at x=14, y=17: closest beacon is at x=10, y=16
      //     Sensor at x=8, y=7: closest beacon is at x=2, y=10
      //     Sensor at x=2, y=0: closest beacon is at x=2, y=10
      //     Sensor at x=0, y=11: closest beacon is at x=2, y=10
      //     Sensor at x=20, y=14: closest beacon is at x=25, y=17
      //     Sensor at x=17, y=20: closest beacon is at x=21, y=22
      //     Sensor at x=16, y=7: closest beacon is at x=15, y=3
      //     Sensor at x=14, y=3: closest beacon is at x=15, y=3
      //     Sensor at x=20, y=1: closest beacon is at x=15, y=3
      //   `,
      //   expected: "26",
      // },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      // {
      //   input: `
      //     Sensor at x=2, y=18: closest beacon is at x=-2, y=15
      //     Sensor at x=9, y=16: closest beacon is at x=10, y=16
      //     Sensor at x=13, y=2: closest beacon is at x=15, y=3
      //     Sensor at x=12, y=14: closest beacon is at x=10, y=16
      //     Sensor at x=10, y=20: closest beacon is at x=10, y=16
      //     Sensor at x=14, y=17: closest beacon is at x=10, y=16
      //     Sensor at x=8, y=7: closest beacon is at x=2, y=10
      //     Sensor at x=2, y=0: closest beacon is at x=2, y=10
      //     Sensor at x=0, y=11: closest beacon is at x=2, y=10
      //     Sensor at x=20, y=14: closest beacon is at x=25, y=17
      //     Sensor at x=17, y=20: closest beacon is at x=21, y=22
      //     Sensor at x=16, y=7: closest beacon is at x=15, y=3
      //     Sensor at x=14, y=3: closest beacon is at x=15, y=3
      //     Sensor at x=20, y=1: closest beacon is at x=15, y=3
      //   `,
      //   expected: "56000011",
      // },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  onlyTests: false,
});
