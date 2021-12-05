const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(5);
  const coords = input.map((line) => {
    const splittedLine = line.split("->").filter(Boolean);
    const from = splittedLine[0];
    const to = splittedLine[1];
    return [
      from.split(",").map((x) => Number(x)),
      to.split(",").map((x) => Number(x)),
    ];
  });
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

  const result = new Array(yMax).fill(0).map(() => new Array(xMax).fill(0));
  coords.forEach((pair) => {
    const from = pair[0];
    const to = pair[1];
    if (from[1] == to[1]) {
      if (from[0] < to[0]) {
        for (i = from[0]; i <= to[0]; i++) {
          result[from[1]][i] += 1;
        }
      } else if (from[0] > to[0]) {
        for (i = from[0]; i >= to[0]; i--) {
          result[from[1]][i] += 1;
        }
      }
    } else if (from[0] == to[0]) {
      if (from[1] < to[1]) {
        for (i = from[1]; i <= to[1]; i++) {
          result[i][from[0]] += 1;
        }
      } else if (from[1] > to[1]) {
        for (i = from[1]; i >= to[1]; i--) {
          result[i][from[0]] += 1;
        }
      }
    } else {
      //
      if (from[0] < to[0] && from[1] < to[1]) {
        for (i = from[0], j = from[1]; i <= to[0]; i++, j++) {
          result[j][i] += 1;
        }
      } else if (from[0] > to[0] && from[1] > to[1]) {
        for (i = from[0], j = from[1]; i >= to[0]; i--, j--) {
          result[j][i] += 1;
        }
      } else if (from[0] > to[0] && from[1] < to[1]) {
        for (i = from[0], j = from[1]; i >= to[0]; i--, j++) {
          result[j][i] += 1;
        }
      } else if (from[0] < to[0] && from[1] > to[1]) {
        for (i = from[0], j = from[1]; i <= to[0]; i++, j--) {
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
