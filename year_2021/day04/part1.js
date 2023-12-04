const fetchInput = require("../fetchInput");

const main = async () => {
  const input = await fetchInput(4);
  const bingoNumbers = input
    .shift()
    .split(",")
    .map((x) => Number(x));
  const boards = [];
  input.shift();
  for (i = 0; i < input.length; i += 6) {
    boards.push(
      input.slice(i, i + 5).map((x) =>
        x
          .split(" ")
          .filter(Boolean)
          .map((x) => Number(x))
      )
    );
  }

  const potentionWinnerBoards = [];
  boards.forEach((board) => {
    for (i = 0; i < board.length; i++) {
      const row = board[i];
      const sum = [];
      row.forEach((e) => {
        const index = bingoNumbers.indexOf(e);
        if (index == -1) {
          return;
        } else {
          sum.push(index);
        }
      });
      if (sum.length == 5) {
        potentionWinnerBoards.push([board, Math.max(...sum), i, null]);
      }
    }

    for (j = 0; j < board.length; j++) {
      const column = [
        board[0][j],
        board[1][j],
        board[2][j],
        board[3][j],
        board[4][j],
      ];

      const sum = [];
      column.forEach((e) => {
        const index = bingoNumbers.indexOf(e);
        if (index == -1) {
          return;
        } else {
          sum.push(index);
        }
      });
      if (sum.length == 5) {
        potentionWinnerBoards.push([board, Math.max(...sum), null, j]);
      }
    }
  });
  let winnerBoard = [];
  let smallestDistance = Number.POSITIVE_INFINITY;
  potentionWinnerBoards.forEach((b) => {
    if (b[1] < smallestDistance) {
      winnerBoard = b;
      smallestDistance = b[1];
    }
  });
  console.log(winnerBoard, "KEK");

  const boardSum = winnerBoard[0].reduce(
    (acc, a) => acc + a.reduce((sum, b) => sum + b, 0),
    0
  );

  let winnerNumberIndex = Number.NEGATIVE_INFINITY;

  if (winnerBoard[2] > 0) {
    console.log(winnerBoard[2]);
    winnerBoard[0][winnerBoard[2]].forEach((n) => {
      const index = bingoNumbers.indexOf(n);
      if (index > winnerNumberIndex) {
        winnerNumberIndex = index;
      }
    });
  } else {
    winnerBoard[0].forEach((_, i) => {
      const index = bingoNumbers.indexOf(winnerBoard[0][i][winnerBoard[3]]);
      if (index > winnerNumberIndex) {
        winnerNumberIndex = index;
      }
    });
  }
  const touchedNumbersSum = winnerBoard[0]
    .flat(2)
    .map((x) => {
      const index = bingoNumbers.slice(0, winnerNumberIndex + 1).indexOf(x);
      if (index != -1) {
        return x;
      }
    })
    .filter((n) => n != undefined)
    .reduce((a, b) => a + b, 0);
  console.log(
    boardSum,
    touchedNumbersSum,
    boardSum - touchedNumbersSum,
    bingoNumbers[winnerNumberIndex]
  );
  console.log(
    "ANSWER: ",
    (boardSum - touchedNumbersSum) * bingoNumbers[winnerNumberIndex]
  );
};

main();
