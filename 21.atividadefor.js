const readline = require("readline-sync")

const num1 = readline.questionInt ("Digite o número pra mostrar a tabuada")


for (let i = 1; i<=10; i++){
    console.log(`${num1} x ${i} = ${num1 * i}`)
}

