const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(8);
  const decodeTable = {
    3: 7,
    2: 1,
    4: 4,
    7: 8,
  };

  let result = 0;
  input.forEach((e) => {
    let [entries, output] = e.replace("\r", "").split(" | ");
    output.split(" ").forEach((d) => {
      if (decodeTable[d.length]) {
        result += 1;
      }
    });
  });
  console.log(result);
};

main();
