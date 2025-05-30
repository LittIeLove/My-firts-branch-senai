const readline = require('readline-sync');


const number = readline.questionInt('Digite o número');

if (number % 2 === 0){
    console.log(`${number} é par`)
} else{
    console.log(`${number} é impar`)
}

