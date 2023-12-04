const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(10);
  console.log(input);
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
  //stack = ["]", ")", }, )]

  input.forEach((row) => {
    const stack = [];
    const arr = row.split("");
    console.log(arr);
    for (i = 0; i < arr.length; i++) {
      const c = arr[i];
      console.log(c);
      console.log(invalidChars.has(c));
      if (stack[stack.length - 1] === c) {
        console.log(
          stack[stack.length - 1] === c,
          "Popping: ",
          stack[stack.length - 1]
        );
        stack.pop();
      } else if (invalidChars.has(c)) {
        console.log("Illegeal character: ", c);
        score += scoreTable[c];
        break;
      } else {
        console.log("Pushing: ", "for C: ", c, validChars[c]);
        stack.push(validChars[c]);
      }
    }
  });
  console.log(score);
};

main();
