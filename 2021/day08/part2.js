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
  input.forEach((ee) => {
    const mapping = {};
    let [entries, output] = ee.replace("\r", "").split(" | ");
    const e = entries.split(" ");

    let eee = [];
    e.forEach((d, i) => {
      if (decodeTable[d.length]) {
        mapping[decodeTable[d.length]] = d;
      } else {
        eee.push(d);
      }
    });
    while (eee.length != 1) {
      console.log("starting my loop");
      for (i = 0; i < eee.length; i++) {
        const d = eee[i];
        if (!mapping[9]) {
          console.log("searching for number 9");
          if (
            d.length === 6 &&
            mapping[4].split("").every((v) => d.includes(v))
          ) {
            mapping[9] = d;
            eee = eee.filter((i) => i != d);
            console.log("found 9", d);
            break;
          }
        } else if (!mapping[0]) {
          console.log("searching for 0");
          if (
            d.length === 6 &&
            mapping[1].split("").every((v) => d.includes(v))
          ) {
            mapping[0] = d;
            eee = eee.filter((i) => i != d);
            console.log("found 0");
            break;
          }
        } else if (!mapping[6]) {
          console.log("searching for 6");
          if (d.length === 6) {
            mapping[6] = d;
            eee = eee.filter((i) => i != d);
            console.log("found 6");
            break;
          }
        } else if (!mapping[5]) {
          console.log("searching for 5");
          if (
            d.length === 5 &&
            d.split("").every((v) => mapping[6].includes(v))
          ) {
            mapping[5] = d;
            eee = eee.filter((i) => i != d);
            console.log("found 5");
            break;
          }
        } else if (!mapping[3]) {
          console.log("searching for 3");
          if (
            d.length === 5 &&
            d.split("").every((v) => mapping[9].includes(v))
          ) {
            mapping[3] = d;
            eee = eee.filter((i) => i != d);
            console.log("found 3");
            break;
          }
        }
      }
    }
    mapping[2] = eee[0];

    let num = "";
    output.split(" ").forEach((o) => {
      for (const [k, v] of Object.entries(mapping)) {
        if (o.split("").sort().join() === v.split("").sort().join()) {
          num += k;
        }
      }
    });
    result += Number(num);
  });
  console.log(result, "alma");
};

main();
