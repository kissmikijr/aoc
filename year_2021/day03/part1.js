const fetchInput = require("../fetchInput")


const main = async () =>{
    const input = await fetchInput(3)
    const result = [[0,0],[0,0],[0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0], [0,0], [0,0], [0,0]]

    input.forEach( (binary)=> {
        [...binary].forEach((d,i) =>{
        if (d == "0") {
            result[i][0] += 1
        } else if (d=="1") {
            result[i][1] += 1
        }

        })

    })
    console.log(result)
    let gammaBinary = ''
    result.forEach(v=>{
        if (v[0] > v[1]) {
            gammaBinary += '0'
        } else {
            gammaBinary += '1'
        }
    })
    let epsilonBinary = ''
    result.forEach(v=>{
        if (v[0] < v[1]) {
            epsilonBinary += '0'
        } else {
            epsilonBinary += '1'
        }
    })
    console.log(gammaBinary, epsilonBinary , parseInt(gammaBinary, 2) * parseInt(epsilonBinary, 2))

}

main()
