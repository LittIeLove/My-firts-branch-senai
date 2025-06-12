document.getElementById("gerador").addEventListener("click",conometrar)

document.getElementById("numero").addEventListener("keydown", function(event){
    if (event.key === "Enter"){
        conometrar();
    }
});

function conometrar(){
    const n1 = parseInt(document.getElementById("numero").value);
    const resultadoTempo = document.getElementById("resultado");
    resultadoTempo.innerHTML = "";

    if(isNaN(numero)){
        resultadoTempo.innerHTML = <span style='color: red;'>Digite um número válido!</span>;
        return;
    }
    let listaHTML = <ul style= 'list-style; none; padding-left: 0;'></ul>;

    for (let i= n1; i = 0; i--){
        listaHTML += <li><strong>${n1}</strong></li>
    }
    listaHTML+= "</ul>";
    resultadoTempo.innerHTML = listaHTML;
}