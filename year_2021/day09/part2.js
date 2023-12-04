const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(9);
  let lowPointsResult = [];
  input.forEach((row, j) => {
    const lowPoints = row.split("").map(Number);

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
      if (p < left && p < right && p < up && p < down) {
        lowPointsResult.push({ index: i, row: j });
      }
    });
  });
  const matrix = input.map((r) => r.split("").map(Number));
  let result = [];
  let visited = {};
  lowPointsResult.forEach((p) => {
    const size = searchBigger(
      matrix[p.row][p.index],
      p.index,
      p.row,
      matrix,
      1,
      visited
    );
    result.push(size);
  });
  console.log(
    result
      .sort((a, b) => a - b)
      .slice(result.length - 3, result.length)
      .reduce((acc, b) => acc * b, 1)
  );
};
function searchBigger(base, i, j, matrix, size, visited) {
  if (visited.hasOwnProperty([i, j])) {
    return size - 1;
  } else {
    visited[[i, j]] = undefined;
  }
  let left = matrix[j][i - 1];
  let right = matrix[j][i + 1];
  let top = matrix[j - 1] ? matrix[j - 1][i] : Number.POSITIVE_INFINITY;
  let down = matrix[j + 1] ? matrix[j + 1][i] : Number.POSITIVE_INFINITY;
  if (
    left !== undefined &&
    left !== 9 &&
    left != Number.POSITIVE_INFINITY &&
    left > base
  ) {
    size = searchBigger(left, i - 1, j, matrix, size + 1, visited);
  }
  if (
    right !== undefined &&
    right !== 9 &&
    right != Number.POSITIVE_INFINITY &&
    right > base
  ) {
    size = searchBigger(right, i + 1, j, matrix, size + 1, visited);
  }
  if (top !== 9 && top > base && top !== Number.POSITIVE_INFINITY) {
    size = searchBigger(top, i, j - 1, matrix, size + 1, visited);
  }
  if (down !== 9 && down !== Number.POSITIVE_INFINITY && down > base) {
    size = searchBigger(down, i, j + 1, matrix, size + 1, visited);
  }
  return size;
}

main();
