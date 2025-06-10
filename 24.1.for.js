const readline = require('readline-sync');

const pares =[]
const impares =[]
const quant = 6

for (let i = 0; i < quant;i++) {
    let numeros = readline.questionInt(`Digite o ${i+1} numero: `)
    if (numeros % 2 ===0){
        pares.push(numeros)
    }else{
        impares.push(numeros)

    }

}
console.log(`Numeros pares:`)
console.log(pares,`  Quantidade =`, pares.length)
console.log(`Numeros impares:`)
console.log(impares,`  Quantidade=`, impares.length)