document.getElementById("gerarBotao").addEventListener("click", gerarTabuada);

document.getElementById("numeroInput").addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    gerarTabuada(); // Chama a função de gerar tabuada ao pressionar Enter
  }
});

function gerarTabuada() {
  const numero = parseInt(document.getElementById("numeroInput").value);
  const resultado = document.getElementById("resultadoTabuada");
  resultado.innerHTML = ""; // Limpa resultado anterior

  if (isNaN(numero)) {
    resultado.innerHTML = "<span style='color: red;'>Digite um número válido!</span>";
    return;
  }

  let listaHTML = "<ul style='list-style: none; padding-left: 0;'>";

  for (let i = 1; i <= 10; i++) {
    listaHTML += `<li><strong>${numero}</strong> × <strong>${i}</strong> = <strong>${numero * i}</strong></li>`;
  }

  listaHTML += "</ul>";
  resultado.innerHTML = listaHTML;
}
d