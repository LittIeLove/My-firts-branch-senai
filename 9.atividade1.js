console.clear()
const readline = require("readline-sync");

const idade = readline.questionInt ('Digite sua idade: ')

if (idade < 16){
    console.log('Não pode votar: ')
} else if (idade < 18){
    console.log('Voto opcional')
} else if(idade < 65){
    console.log('Voto obrigatório')
} else{
    console.log ('Voto não obrigatório')
}




