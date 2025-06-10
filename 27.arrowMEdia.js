const readline = require('readline-sync');

const numbers = []

for(let i = 0; i<3;i++){
    num = readline.questionFloat(`Digite o ${i+1} numero: `)
    numbers.push(num)

}

const media = numbers.reduce((acumlador, valorAtual)=>{return acumlador + valorAtual })

console.log(`A media dos numero: `,numbers, ` e = `, media / 3 )