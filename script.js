const imagens = ["img/Banner1.PNG", "img/Banner2.PNG"];
let indiceAtual = 0;

function mudarImagem() {
  const imagem = document.getElementById("imagemDinamica");
  imagem.classList.add("hidden");

  setTimeout(function () {
    indiceAtual = (indiceAtual + 1) % imagens.length;
    imagem.src = imagens[indiceAtual];
    imagem.alt = "img/Banner" + (indiceAtual + 1);

    setTimeout(function () {
      imagem.classList.remove("hidden");
    }, 100); 
  }, 500); 
}

setInterval(mudarImagem, 10000);
