const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(7);
  const positions = input[0].split(",").map(Number);
  const maxPos = Math.max(...new Set(positions));
  const fuels = [];
  for (i = 0; i <= maxPos; i++) {
    let fuel = 0;
    positions.forEach((p) => {
      for (j = 0; j <= Math.abs(i - p); j++) {
        fuel += j;
      }
    });
    fuels.push(fuel);
  }
  console.log(Math.min(...fuels));
};

main();
