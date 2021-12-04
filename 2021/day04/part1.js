const fetchInput = require("../fetchInput")


const main = async () =>{
    const input = await fetchInput(4)
    const bingoNumbers = input.shift().split(",").map(x=>Number(x))
    const boards = []
    input.shift()
    for (i=0; i < input.length; i+=6) {
        boards.push(input.slice(i, i+5).map(x=>x.split(" ").filter(Boolean).map(x=>Number(x))))
    }
    console.log(boards, bingoNumbers)

}

main()
