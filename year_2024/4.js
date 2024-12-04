const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString();

const searchX = ({ y, x, grid }) => {
  let r = 0;
  const length = grid.length - 1;
  if (x + 3 <= length) {
    // ->
    if (grid[y][x + 1] === "M") {
      if (grid[y][x + 2] === "A") {
        if (grid[y][x + 3] === "S") {
          r += 1;
        }
      }
    }
  }
  if (x - 3 >= 0) {
    // <-
    if (grid[y][x - 1] === "M") {
      if (grid[y][x - 2] === "A") {
        if (grid[y][x - 3] === "S") {
          r += 1;
        }
      }
    }
  }
  if (y - 3 >= 0) {
    // ^
    if (grid[y - 1][x] === "M") {
      if (grid[y - 2][x] === "A") {
        if (grid[y - 3][x] === "S") {
          r += 1;
        }
      }
    }
  }
  if (y + 3 <= length) {
    // v
    if (grid[y + 1][x] === "M") {
      if (grid[y + 2][x] === "A") {
        if (grid[y + 3][x] === "S") {
          r += 1;
        }
      }
    }
  }
  if (y + 3 <= length && x + 3 <= length) {
    // -> ^
    if (grid[y + 1][x + 1] === "M") {
      if (grid[y + 2][x + 2] === "A") {
        if (grid[y + 3][x + 3] === "S") {
          r += 1;
        }
      }
    }
  }
  if (y + 3 <= length && x - 3 >= 0) {
    // v <-
    if (grid[y + 1][x - 1] === "M") {
      if (grid[y + 2][x - 2] === "A") {
        if (grid[y + 3][x - 3] === "S") {
          r += 1;
        }
      }
    }
  }
  if (y - 3 >= 0 && x - 3 >= 0) {
    // ^ <-
    if (grid[y - 1][x - 1] === "M") {
      if (grid[y - 2][x - 2] === "A") {
        if (grid[y - 3][x - 3] === "S") {
          r += 1;
        }
      }
    }
  }
  if (y - 3 >= 0 && x + 3 <= length) {
    // -> v
    if (grid[y - 1][x + 1] === "M") {
      if (grid[y - 2][x + 2] === "A") {
        if (grid[y - 3][x + 3] === "S") {
          r += 1;
        }
      }
    }
  }
  return r;
};
const p1 = () => {
  let result = 0;
  const term = "XMAS";
  const grid = input.split("\n").map((l) => l.split(""));
  for (let y = 0; y < grid.length; y++) {
    const line = grid[y];
    for (let x = 0; x < line.length; x++) {
      const cell = line[x];
      if (cell === "X") {
        result += searchX({ x, y, grid });
      }
    }
  }
  console.log("P1: ", result);
};
p1();

const searchA = ({ y, x, grid }) => {
  let r = 0;
  const length = grid.length - 1;

  if (y + 1 <= length && x + 1 <= length && x - 1 >= 0 && y - 1 >= 0) {
    if (
      // -> ^
      grid[y + 1][x + 1] === "M" &&
      grid[y + 1][x - 1] === "S" &&
      grid[y - 1][x - 1] === "S" &&
      grid[y - 1][x + 1] === "M"
    ) {
      return 1;
    } else if (
      grid[y + 1][x + 1] === "S" &&
      grid[y + 1][x - 1] === "S" &&
      grid[y - 1][x - 1] === "M" &&
      grid[y - 1][x + 1] === "M"
    ) {
      return 1;
    } else if (
      grid[y + 1][x + 1] === "M" &&
      grid[y + 1][x - 1] === "M" &&
      grid[y - 1][x - 1] === "S" &&
      grid[y - 1][x + 1] === "S"
    ) {
      return 1;
    } else if (
      grid[y + 1][x + 1] === "S" &&
      grid[y + 1][x - 1] === "M" &&
      grid[y - 1][x - 1] === "M" &&
      grid[y - 1][x + 1] === "S"
    ) {
      return 1;
    }
  }

  return r;
};
const p2 = () => {
  let result = 0;
  const term = "XMAS";
  const grid = input.split("\n").map((l) => l.split(""));
  for (let y = 0; y < grid.length; y++) {
    const line = grid[y];
    for (let x = 0; x < line.length; x++) {
      const cell = line[x];
      if (cell === "A") {
        result += searchA({ x, y, grid });
      }
    }
  }
  console.log("P2: ", result);
};
p2();
