const readline = require("readline-sync")

let num1 = readline.questionFloat("Digite")
while(num1){
    if (num1 <0 || num1 > 10){
         num1 = readline.questionFloat("Digite")
        } else{
            break
        }
        
}

