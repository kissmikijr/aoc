const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString();
const exampleData = `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`;
const exampleData2 = `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`;
// let lines = input.split("\n").map((l) => l.split(" ").map((n) => Number(n)));

lines = input;
let result = 0;
const matches = [...lines.matchAll(/mul\(\d?\d?\d,\d?\d?\d\)/g)];
matches.forEach((m) => {
  const digitsMatcher = [...m[0].matchAll(/\d?\d?\d,\d?\d?\d/g)];
  digitsMatcher.forEach((dm) => {
    const ds = dm[0].split(",");
    result += Number(ds[0]) * Number(ds[1]);
  });
});
console.log("p1: ", result);

const p2 = () => {
  let res = 0;
  const doRegex = /do\(\)/g;
  const doNotRegex = /don't\(\)/g;
  const mulRegex = /mul\(\d?\d?\d,\d?\d?\d\)/g;

  const matches = [
    ...lines.matchAll(doRegex),
    ...lines.matchAll(doNotRegex),
    ...lines.matchAll(mulRegex),
  ].sort((a, b) => {
    return a.index - b.index;
  });

  let enabled = true;
  matches.forEach((match) => {
    if (match[0].startsWith("mul")) {
      if (enabled) {
        const digitsMatcher = [...match[0].matchAll(/\d?\d?\d,\d?\d?\d/g)];
        digitsMatcher.forEach((dm) => {
          const ds = dm[0].split(",");
          res += Number(ds[0]) * Number(ds[1]);
        });
      }
    } else if (match[0] === "do()") {
      enabled = true;
    } else if (match[0] === "don't()") {
      enabled = false;
    }
  });
  console.log(res, "p2");
};
p2();
