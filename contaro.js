function obterValoresDoFormulario() {
    // Obter valores do formulário
    const dadosDoFormulario = {
        nomeSobrenome: document.getElementById("nomesobrenome").value,
        email: document.getElementById("Email").value,
        telefone: document.getElementById("telefone").value,
        mensagem: document.getElementById("mensagem").value,
        contatoPreferido: document.querySelector('input[name="contato"]:checked').value,
        horarioPreferido: document.querySelector('select').value,
        receberNovidades: document.querySelector('input[type="checkbox"]').checked
    };

    // Exibir os dados no console
    console.log(dadosDoFormulario);

    // Enviar os dados para a API
    enviarParaAPI(dadosDoFormulario);
}

function enviarParaAPI(dados) {
    const url = 'http://127.0.0.1:5000/enviarFormulario';

    // Configurar opções para a requisição
    const options = {
        method: 'POST', // ou 'PUT', 'DELETE', etc., dependendo da sua API
        headers: {
            'Content-Type': 'application/json'
            // Adicione outros headers necessários aqui
        },
        body: JSON.stringify(dados)
    };

    // Enviar a requisição para a API usando fetch
    fetch(url, options)
        .then(response => response.json())
        .then(data => console.log('Resposta da API:', data))
        .catch(error => console.error('Erro ao enviar para a API:', error));
}
