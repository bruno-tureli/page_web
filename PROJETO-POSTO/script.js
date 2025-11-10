function calcular_melhor_preco() {  // Função sem parâmetro


// declarada a variavel que recebe a captura da ID - Alcool  ln. 33 (index) 
let preco_alcool = document.getElementById('alcool').value // .value captura qualquer valor passado no formulário
// declarada a variavel que recebe a captura da ID - Alcool  ln. 39 (index) 
let preco_gasolina = document.getElementById('alcool').value 

if (preco_alcool != " ") {

    if (preco_gasolina != " ") {

let resultado = preco_alcool / preco_gasolina

if (resultado >= 0.7) {
    alert("Melhor utilizar gasolina")
// document.GetElementById('resultado').innerHTML = "Melhor utilizar a gasolina"
// ln. 42
} else {
    alert("melhor utilizar alcool") 
// document.GetElementById('resultado').innerHTML = "Melhor utilizar o alcool"
// ln. 42
}

} else {
    alert("Preencha o campo do alcool")
}


} else {
    alert("Preencha o campo da gasolina")
}

}

// Validacao de campos

// Declarada as variaveis dentro da função "calcular_melhor_preço *ln. 45"
// Passou a condicao se o(s) campo(s) estiver(em) vazio(s), é exibido na tela 
// para o usuário preencher o(s) respectrivo(s) campo(s)

// Logo é passado a condicao para ver qual é o melhor combustivel para ser usado
// O resultado da comparacao é exibida na tela para o usuario.

// A interacao com usuario é pelo evento onclick "Calcular" ln. 44, 45 e 46   