const readline = require('readline-sync');

const numbers = []
const pares =[]
const impares =[]
const quant = 6
let par =0
let impar = 0

for (let i = 0; i < quant;i++) {
    let numeros = readline.questionInt(`Digite o ${i+1}ª número`)
    numbers.push(numeros)
    if (numeros % 2 ===0){
        pares.push(numeros)
    }else{
        impares.push(numeros)

    }

}
for (let i= 0; i< numbers.length;i++){
    if (numbers[i] % 2 === 0){
        par += 1
    } else{
        impar += 1
    }
}

console.log(`Existem no vetor ${par} números pares`)
console.log(`Existem no vetor ${impar} números impares\n`)
console.log(`Números pares:`)
console.log(pares)
console.log(`Números impares:`)
console.log(impares)