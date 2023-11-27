// getURL.js
const avatar1 = "https://cdn.imgbin.com/6/19/3/imgbin-pepe-the-frog-youtube-meme-video-drawception-youtube-7A8dZRLY7iDjafL3d9DFfnC6h.jpg";
const avatar2 = "https://tr.rbxcdn.com/58ff075820895bda7b0422f7e7f3b4fa/420/420/Hat/Png"; 
const avatar3 = "https://w7.pngwing.com/pngs/878/763/png-transparent-squidward-tentacles-internet-meme-know-your-meme-meme-hand-sticker-cartoon-thumbnail.png";
const avatar4 = "https://tr.rbxcdn.com/dd2b1a2bb310f1401b3eb9eeb243cf70/420/420/Image/Png";
const avatar5 = "https://e7.pngegg.com/pngimages/378/59/png-clipart-old-school-runescape-internet-meme-youtube-random-game-child-thumbnail.png";
const avatar6 = "https://m.media-amazon.com/images/I/71UdPXPpjoL.png";
const avatar7 = "https://gifs.eco.br/wp-content/uploads/2023/05/imagens-de-cachorro-meme-png-1.png";
const avatar8= "https://venngage-wordpress.s3.amazonaws.com/uploads/2022/09/meme_awkward_look_monkey_puppet.png";
const listaImagens = [avatar1, avatar2, avatar3, avatar4, avatar5,avatar6,avatar7,avatar8];

function imagemAleatoria() {
  const indiceAleatorio = Math.floor(Math.random() * listaImagens.length);
  return listaImagens[indiceAleatorio];
}
// comentariosArray[i].nome   comentariosArray[i].comentario
function criarComentario(imagem,name,comment) {
    var container = document.getElementById("container")
    
    var divElement = document.createElement("div");
    divElement.className = "my-3 p-3 bg-white rounded shadow-sm";

    var h6Element = document.createElement("h6");
    h6Element.className = "border-bottom border-gray pb-2 mb-0";


    var mediaDivElement = document.createElement("div");
    mediaDivElement.className = "media text-muted pt-3";

    var imgElement = document.createElement("img");
    imgElement.setAttribute("data-src", "holder.js/32x32?theme=thumb&amp;bg=007bff&amp;fg=007bff&amp;size=1");
    imgElement.alt = "32x32";
    imgElement.className = "mr-2 rounded";
    imgElement.src = imagem;
    imgElement.setAttribute("data-holder-rendered", "true");
    imgElement.style.width = "32px";
    imgElement.style.height = "32px";

    var pElement = document.createElement("p");
    pElement.className = "media-body pb-3 mb-0 small lh-125 border-bottom border-gray";

    var strongElement = document.createElement("strong");
    strongElement.className = "d-block text-gray-dark";
    strongElement.textContent =name;

    var textNode = document.createTextNode(comment);

    // Adicionar elementos ao DOM
    container.appendChild(divElement);
    divElement.appendChild(h6Element);
    divElement.appendChild(mediaDivElement);
    mediaDivElement.appendChild(imgElement);
    mediaDivElement.appendChild(pElement);
    pElement.appendChild(strongElement);
    pElement.appendChild(textNode);
}

// Função para obter o parâmetro da URL por nome
function getURLParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}
const projetoParam = getURLParameter('projeto');

// Função para redirecionar com base no valor do parâmetro 'projeto'
function redirectToAPIRoute() {


    if (projetoParam) {
        const apiUrl = 'http://127.0.0.1:5000/';

        switch (projetoParam) {
            case '1':
                makeApiRequest(apiUrl + 'City-Sewer');
                break;
            case '2':
                makeApiRequest(apiUrl + 'Water-Responsible');
                break;
            case '3':
                makeApiRequest(apiUrl + 'Solid-Waste');
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
        success: function (data) {

            var tagHtml0 = document.getElementById("titleText");
            var conteudoHTML = data.title;
            tagHtml0.innerHTML = conteudoHTML;

            var tagHtml1 = document.getElementById("introducaoText");
            var conteudoHTML = data.introduction;
            tagHtml1.innerHTML = conteudoHTML;

            var tagHtml2 = document.getElementById("DesenvolvimentoText1");
            var conteudoHTML = data.paragraph1;
            tagHtml2.innerHTML = conteudoHTML;

            var tagHtml3 = document.getElementById("DesenvolvimentoText2");
            var conteudoHTML = data.paragraph2;
            tagHtml3.innerHTML = conteudoHTML;

            var tagHtml4 = document.getElementById("comclusaoText");
            var conteudoHTML = data.conclusion;
            tagHtml4.innerHTML = conteudoHTML;


            var comentariosArray = data.comentario;

            for (var i = 0; i < comentariosArray.length; i++) {
                criarComentario(imagemAleatoria(),comentariosArray[i].nome,comentariosArray[i].comentario)
            }

            console.log('Resposta da API:', data);
            // Adicione aqui o código para manipular a resposta JSON conforme necessário
        },
        error: function (xhr, status, error) {
            console.error('Erro na solicitação à API:', status, error);
        }
    });
}

function adicionarComentario() {
    // Obter os valores do formulário
    var nome = document.getElementById('nome').value;
    var comentario = document.getElementById('comentario').value;
    console.log(nome, comentario)
    // Validar se ambos os campos foram preenchidos
    if (nome && comentario) {
        // Criar um objeto com os dados do comentário
        var dadosComentario = {
            nome: nome,
            comentario: comentario,
            numero: projetoParam
        };

        // Enviar os dados para a rota http://192.168.2.106:5000/adicionar_comentario
        $.ajax({
            url: 'http://127.0.0.1:5000/adicionar_comentario',
            type: 'POST', // ou 'GET' dependendo do seu servidor
            contentType: 'application/json',
            data: JSON.stringify(dadosComentario),
            success: function (response) {
                // O servidor pode responder com alguma confirmação, se necessário
                console.log(response);
                const name = document.getElementById('nome');
                const comment = document.getElementById('comentario');
                criarComentario(imagemAleatoria(),name.value,comment.value)

                // Limpar os campos do formulário
                name.value = '';
                comment.value = '';

            },
            error: function (error) {
                console.error("Erro na requisição AJAX", error);
            }
        });
    } else {
        alert("Por favor, preencha todos os campos.");
    }

}


// Chamar a função ao carregar a página

redirectToAPIRoute();