const fetchInput = require("../fetchInput")


const main = async () =>{
    const input = await fetchInput(2)
    let horizontalPos = 0
    let depth = 0
    let aim = 0

    input.forEach(instruction =>{
        const command = instruction.split(" ")[0]
        const value = Number(instruction.split(" ")[1])

        switch (command) {
            case "forward":
                horizontalPos += value
                depth += aim * value
                break
            case "down":
                aim += value
                break
            case "up":
                aim -= value
                break
            default:
                console.log(command)
        }

    })
    console.log(horizontalPos * depth)
}

main()
