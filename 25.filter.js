// Criando um vetor com números.
const listaDeNumeros = [1, 2, 3, 4, 5]

console.log('Listando todos os valores da lista: ')
console.log(listaDeNumeros) // Outputs: [1, 2, 3, 4, 5]

console.log('\nMultiplicando valores por 2:')
const dobrados = listaDeNumeros.map(numero => numero * 2)
console.log(dobrados) // Outputs: [2, 4, 6, 8, 10]

console.log('\nFiltrando elementos pares:')
const pares = listaDeNumeros.filter(numero => numero % 2 === 0)
console.log(pares) // Outputs: [2, 4]

console.log('\nSomando todos os números:')
const soma = listaDeNumeros.reduce((soma, atual) => soma + atual)
console.log(soma) // Outputs: 15

