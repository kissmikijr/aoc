const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(7);
  const positions = input[0].split(",").map(Number);
  const positionTyps = new Set(positions);

  const fuels = [];
  positionTyps.forEach((t) => {
    let fuel = 0;
    positions.forEach((p) => {
      fuel += Math.abs(t - p);
    });
    fuels.push(fuel);
  });
  console.log;
  console.log(Math.min(...fuels));
};

main();
