const readline = require('readline-sync');

const numbers = []

for (let i = 0; i <5; i++ ){
    numeros = readline.questionFloat(`Digite o ${i+1} numero:`)
    numbers.push(numeros)
    
}
console.clear()
const negativos = numbers.filter(numero => numero < 0);
const positivos = numbers.filter(numero => numero> 0);


console.log("Quantidade de numeros negativos",negativos.length)
const soma_positvos = positivos.reduce((acumulador, valorAtual) => {return acumulador + valorAtual;});

console.log(`Soma dos positivos: ${soma_positvos}`)