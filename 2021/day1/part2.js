const fetchInput = require("../fetchInput")


const main = async () =>{
    const input = await fetchInput(1)

    let increasedCounter = 0
    let previousSum = input.slice(0, 3).reduce((acc, a)=>(acc+Number(a)), 0)

    input.shift()

    input.forEach((_, i)=>{
        const currentSum = input.slice(i, i+3).reduce((acc, a)=> (acc+ Number(a)),0)
        if (currentSum.length < 3) {
            return
        } 
        if (currentSum > previousSum) {
            increasedCounter++
        }
        previousSum = currentSum

    })

    console.log(increasedCounter)

}

main()
