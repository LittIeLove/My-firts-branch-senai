const readline = require('readline-sync')

function calculadora(){
    console.log("-------------------------------------");
    console.log("          CALCULADORA SIMPLES        ");
    console.log("-------------------------------------");
    
    // 1. Pedir o primeiro número
    const num1 = readline.questionFloat('Digite o primeiro numero');

    // 2. Pedir o segundo número
    const num2 = readline.questionFloat('Digite o segundo numero');

    // 3. pedir a operação
    console.log('\nEscolha a operação:');
    console.log('1- Adição');
    console.log('2- Subtração');
    console.log('3- Multiplicação');
    console.log('4- Divisão');
    const operacao = readline.questionInt('Digite a operação desejada');

    let resultado;
    let operacao_valida = true;

    switch (operacao){
        case 1:
            resultado = num1 + num2
            console.log (`${num1} + ${num2} = ${resultado}`);
            break
        case 2:
            resultado = num1 - num2
            console.log (`${num1} - ${num2} = ${resultado}`);
            break
        case 3:
            resultado = num1 * num2
            console.log (`${num1} * ${num2} = ${resultado}`);
            break
        case 4:
            if (num2 === 0) {
                console.log('Erro: Divisão por zero não é válida.');
                operacaoValida = false;
                
            } else {
                resultado = num1 / num2;
                console.log(`${num1} / ${num2} = ${resultado}`);
            }
            break
        default:
            if (operacao_valida === false){
                console.log('Valor invalido')
                break
            }
            

    }
}

calculadora()



