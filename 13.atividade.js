const readline = require('readline-sync')

const number = readline.questionInt('Digite o número do dia da semana')

switch(number){
    case 1:
    case 7:
        console.log('Final de semana')
        break
    case 2:          
    case 3:
    case 4:
    case 5:
    case 6:
        console.log('Dia Útil')    
        break
    default:
        console.log('Digito invalido')
        break
}

        