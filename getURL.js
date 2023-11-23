// getURL.js

// Função para obter o parâmetro da URL por nome
function getURLParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Função para redirecionar com base no valor do parâmetro 'projeto'
function redirectToAPIRoute() {
    const projetoParam = getURLParameter('projeto');

    if (projetoParam) {
        const apiUrl = 'http://192.168.2.106:5000/';

        switch (projetoParam) {
            case '1':
                makeApiRequest(apiUrl + 'City_Sewer');
                break;
            case '2':
                makeApiRequest(apiUrl + 'Water_Responsible');
                break;
            case '3':
                makeApiRequest(apiUrl + 'Solid_Waste');
                break;
            default:
                console.error('Projeto não reconhecido:', projetoParam);
        }
    } else {
        console.error('Parâmetro "projeto" não encontrado na URL.');
    }
}

// Função para fazer uma solicitação à API e manipular a resposta JSON
function makeApiRequest(apiUrl) {
    $.ajax({
        url: apiUrl,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            alert(data)
// conteúdo HTML = 'Introdução: $data.introduction <br> Paragrafo 1: $data.paragraph1 \n Paragrafo 2: $data.paragraph2';
            console.log('Resposta da API:', data);
            // Adicione aqui o código para manipular a resposta JSON conforme necessário
        },
        error: function(xhr, status, error) {
            console.error('Erro na solicitação à API:', status, error);
        }
    });
}

// Chamar a função ao carregar a página
makeApiRequest();
redirectToAPIRoute();
