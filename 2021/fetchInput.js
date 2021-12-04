const axios = require("axios");
const fs = require("fs");
const path = require("path");

require("dotenv").config();

module.exports = async (day) => {
  let input;
  if (fs.existsSync(path.join(process.cwd(), "test_input.txt"))) {
    input = fs.readFileSync(
      path.join(process.cwd(), "test_input.txt"),
      "utf-8"
    );
  } else if (fs.existsSync(path.join(process.cwd(), "input.txt"))) {
    input = fs.readFileSync(path.join(process.cwd(), "input.txt"), "utf-8");
  } else {
    const response = await axios.get(
      `https://adventofcode.com/2021/day/${day}/input`,
      {
        headers: {
          cookie: `session=${process.env.AOC_SESSION_ID}`,
        },
      }
    );
    fs.writeFileSync(path.join(process.cwd(), "input.txt"), response.data);
    input = response.data;
  }

  return input.split("\n");
};
