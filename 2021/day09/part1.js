const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(9);
  let result = 0;
  input.forEach((row, j) => {
    const lowPoints = row.split("").map(Number);
    console.log(lowPoints);

    let prevRow;
    if (input[j - 1]) {
      prevRow = input[j - 1].split("").map(Number);
    }
    let nextRow;
    if (input[j + 1]) {
      nextRow = input[j + 1].split("").map(Number);
    }

    lowPoints.forEach((p, i) => {
      let right = lowPoints[i + 1];
      if (right === undefined) {
        right = Number.POSITIVE_INFINITY;
      }
      let left = lowPoints[i - 1];
      if (left === undefined) {
        left = Number.POSITIVE_INFINITY;
      }
      let up = Number.POSITIVE_INFINITY;
      if (prevRow) {
        up = prevRow[i];
      }
      let down = Number.POSITIVE_INFINITY;
      if (nextRow) {
        down = nextRow[i];
      }
      //   console.log(p, left, right, up, down);
      //   console.log(
      //     "p: ",
      //     p,
      //     "right: ",
      //     right,
      //     "left: ",
      //     left,
      //     "up: ",
      //     up,
      //     "down: ",
      //     down,
      //     "i: ",
      //     i
      //   );
      if (p < left && p < right && p < up && p < down) {
        console.log(p, "Low point");
        result += p + 1;
      }
    });
  });
  console.log(result);
};

main();
