const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(6);
  const daysToRun = 256;
  let currentDay = 0;
  let fishes = input[0].split(",").map(Number);
  while (currentDay < daysToRun) {
    console.log(currentDay);
    let fishesToAdd = 0;
    let newGenFishes = [];
    fishes.forEach((f) => {
      if (f == 0) {
        newGenFishes.push(6);
        fishesToAdd += 1;
      } else {
        newGenFishes.push(f - 1);
      }
    });
    for (i = 0; i < fishesToAdd; i++) {
      newGenFishes.push(8);
    }
    fishes = newGenFishes;
    currentDay += 1;
  }
  console.log(fishes.length);
};

main();
