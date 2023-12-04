const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(10);
  const validChars = {
    "<": ">",
    "(": ")",
    "{": "}",
    "[": "]",
  };
  const invalidChars = new Set([">", ")", "}", "]"]);
  const scoreTable = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
  };

  let score = 0;
  const remainingLines = [];
  input.forEach((row) => {
    const stack = [];
    const arr = row.split("");
    remainingLines.push(arr);
    for (i = 0; i < arr.length; i++) {
      const c = arr[i];
      if (stack[stack.length - 1] === c) {
        stack.pop();
      } else if (invalidChars.has(c)) {
        score += scoreTable[c];
        remainingLines.pop();
        break;
      } else {
        stack.push(validChars[c]);
      }
    }
  });

  const scores = [];
  const part2ScoreTable = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
  };
  remainingLines.forEach((row) => {
    const stack = [];
    row.forEach((c) => {
      if (stack[stack.length - 1] === c) {
        stack.pop();
      } else {
        stack.push(validChars[c]);
      }
    });
    let score = 0;
    stack.reverse().forEach((s) => {
      score *= 5;
      score += part2ScoreTable[s];
    });
    scores.push(score);
  });

  console.log(scores.sort((a, b) => a - b)[(scores.length - 1) / 2]);
};

main();
