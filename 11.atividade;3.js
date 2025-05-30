const readline = require('readline-sync');

const num1 = readline.questionInt('Digite o primeiro número: ');
const num2 = readline.question('Digite o segundo número: ');
const num3 = readline.questionInt('Digite o Terceiro número: ');

if (num1 + num2 > num3){
    console.log(`${num1} +  ${num2} é maior que ${num3}`)
} else if (num1 + num2 === num3){
    console.log('São iguais')
}else{
    console.log(`${num1} + ${num2} é menor que ${num3}`)
}




