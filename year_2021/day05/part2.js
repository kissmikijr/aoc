const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(5);
  // parse input
  const coords = input.map((line) => {
    const splittedLine = line.split("->").filter(Boolean);
    const from = splittedLine[0];
    const to = splittedLine[1];
    return [
      from.split(",").map((x) => Number(x)),
      to.split(",").map((x) => Number(x)),
    ];
  });

  //find size of matrix
  const xCoords = [];
  const yCoords = [];
  coords.forEach((e) => {
    xCoords.push(e[0][0]);
    xCoords.push(e[1][0]);

    yCoords.push(e[0][1]);
    yCoords.push(e[1][1]);
  });
  const xMax = Math.max(...xCoords) + 1;
  const yMax = Math.max(...yCoords) + 1;

  //initialize the given size of matrix with zeros
  const result = new Array(yMax).fill(0).map(() => new Array(xMax).fill(0));

  coords.forEach((coord) => {
    let [x1, y1] = coord[0];
    let [x2, y2] = coord[1];
    if (y1 == y2) {
      if (x1 < x2) {
        for (i = x1; i <= x2; i++) {
          result[y1][i] += 1;
        }
      } else if (x1 > x2) {
        for (i = x1; i >= x2; i--) {
          result[y1][i] += 1;
        }
      }
    } else if (x1 == x2) {
      if (y1 < y2) {
        for (i = y1; i <= y2; i++) {
          result[i][x1] += 1;
        }
      } else if (y1 > y2) {
        for (i = y1; i >= y2; i--) {
          result[i][x1] += 1;
        }
      }
    } else {
      //diagonal
      if (x1 < x2 && y1 < y2) {
        for (i = x1, j = y1; i <= x2; i++, j++) {
          result[j][i] += 1;
        }
      } else if (x1 > x2 && y1 > y2) {
        for (i = x1, j = y1; i >= x2; i--, j--) {
          result[j][i] += 1;
        }
      } else if (x1 > x2 && y1 < y2) {
        for (i = x1, j = y1; i >= x2; i--, j++) {
          result[j][i] += 1;
        }
      } else if (x1 < x2 && y1 > y2) {
        for (i = x1, j = y1; i <= x2; i++, j--) {
          result[j][i] += 1;
        }
      }
    }
  });

  let numberOfOverlaps = 0;
  result.forEach((row) => {
    row.forEach((e) => {
      if (e > 1) {
        numberOfOverlaps += 1;
      }
    });
  });
  console.log(numberOfOverlaps);
};

main();
