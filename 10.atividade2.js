console.clear()
const readline = require('readline-sync')

const num1 = readline.questionFloat('Digite o primeiro número: ')
const num2 = readline.questionFloat('Digite o segundo número: ')

let resultado;
if (num1 === num2){
    resultado = num1 + num2
    console.log (`${num1} + ${num2} = ${resultado}`)
} else{
    resultado = num1 * num2
    console.log (`${num1} * ${num2} = ${resultado}`)
}
