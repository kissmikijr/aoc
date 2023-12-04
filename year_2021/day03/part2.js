const fetchInput = require("../fetchInput")

const main = async () =>{
    const input = await fetchInput(3)
    const o2 = oxygenGenerator(input, 0, '')
    const co2 = co2Scrubber(input, 0, '')
    console.log(o2, co2, o2 * co2)

}
const oxygenGenerator = (input, index, filter) =>{
    if (input.length == 1 ) {
        console.log("DONE: ", parseInt(input, 2))
        return parseInt(input, 2)
    }
    const result = [[0,0],[0,0],[0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0], [0,0], [0,0], [0,0]]


    input.forEach( (binary)=> {
        if (binary[index] == "0") {
            result[index][0] += 1
        } else if (binary[index]=="1") {
            result[index][1] += 1
        }

    })

    if (result[index][0] > result[index][1]) {
        filter += '0'
    } else if (result[index][0] < result[index][1]) {
        filter += '1'
    } else {
        filter += '1'
    }

    return oxygenGenerator(input.filter((v)=>v.startsWith(filter)), index+1, filter)

}
const co2Scrubber = (input, index, filter) =>{
    if (input.length == 1 ) {
        console.log("DONE: ", parseInt(input, 2))
        return parseInt(input, 2)
    }
    const result = [[0,0],[0,0],[0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0], [0,0], [0,0], [0,0]]


    input.forEach( (binary)=> {
        if (binary[index] == "0") {
            result[index][0] += 1
        } else if (binary[index]=="1") {
            result[index][1] += 1
        }

    })

    if (result[index][0] < result[index][1]) {
        filter += '0'
    } else if (result[index][0] > result[index][1]) {
        filter += '1'
    } else {
        filter += '0'
    }

    return co2Scrubber(input.filter((v)=>v.startsWith(filter)), index+1, filter)

}

main()
