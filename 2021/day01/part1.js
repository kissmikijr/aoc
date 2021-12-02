const fetchInput = require("../fetchInput")


const main = async () =>{
    const input = await fetchInput(1)

    let increasedCounter = 0
    let lastValue = Number(input.shift())

    input.forEach(e => {
        if (Number(e) > lastValue) {
            increasedCounter++
        }
        lastValue = Number(e)
    })
    console.log(increasedCounter)
}

main()
