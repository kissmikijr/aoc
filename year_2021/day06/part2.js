const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(6);
  const daysToRun = 256;
  let fishes = input[0].split(",").map(Number);
  const days = new Array(daysToRun).fill(0);
  fishes.forEach((f) => {
    days[f] += 1;
  });
  days.forEach((v, i) => {
    days[i + 7] += days[i];
    days[i + 9] += days[i];
  });
  console.log(days.filter(Number).reduce((a, b) => a + b, 0) + fishes.length);
};

main();
