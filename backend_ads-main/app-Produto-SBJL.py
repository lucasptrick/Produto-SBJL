from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/')
def OK():
    return 'OK'

projetos = [
    {
        "title":'Tratamento de Esgoto da Cidade',
        "introduction": "No cenário contemporâneo, a gestão eficiente dos recursos naturais tornou-se imperativa para o desenvolvimento sustentável das comunidades. Nesse contexto, o Projeto de Tratamento de Esgoto da Cidade emerge como uma iniciativa visionária que não apenas aborda as crescentes preocupações ambientais, mas também promove uma transformação significativa na qualidade de vida dos habitantes locais. Ao implementar um sistema de tratamento de esgoto inovador, este projeto representa um marco crucial na busca por soluções ambientais e destaca-se como um exemplo inspirador de como a engenhosidade humana pode ser canalizada para promover a harmonia entre a urbanização e a preservação do meio ambiente.",
        "paragraph1": "O sistema de tratamento de esgoto de última geração adotado no projeto revela-se uma resposta eficaz às preocupações cada vez mais prementes relacionadas à poluição dos rios e à qualidade da água na cidade. Ao longo de um período de dedicada pesquisa e desenvolvimento, a equipe responsável conseguiu conceber e implementar um sistema que não apenas reduziu de forma significativa a poluição dos rios locais, mas também promoveu uma melhoria notável na qualidade da água. Esse avanço não só beneficiou a vida aquática, proporcionando ecossistemas mais saudáveis, mas também assegurou água potável de alta qualidade para o consumo humano. A dedicação incansável da equipe em tornar esse projeto uma realidade reflete-se nos resultados tangíveis que agora contribuem para a prosperidade e sustentabilidade da comunidade.",
        "paragraph2": "Além disso, o Projeto de Tratamento de Esgoto da Cidade não se limita a mitigar os impactos ambientais negativos; ele atua como um agente catalisador para o desenvolvimento sustentável. A implementação bem-sucedida do sistema não apenas elevou a qualidade de vida dos residentes, proporcionando um ambiente mais limpo e saudável, mas também abriu caminho para a construção de uma comunidade mais consciente e proativa em relação à preservação ambiental. Este projeto não apenas representa uma realização técnica, mas também um modelo inspirador para outras localidades enfrentando desafios semelhantes, reforçando a ideia de que investir em soluções ecologicamente sustentáveis é vital para o progresso a longo prazo.",
        "conclusion": "Em suma, o Projeto de Tratamento de Esgoto da Cidade é um exemplo eloquente de como a inovação e o comprometimento podem convergir para resolver desafios ambientais complexos. Ao transformar a maneira como a cidade lida com o esgoto, não apenas mitigamos os danos causados à natureza, mas também pavimentamos o caminho para uma comunidade mais resiliente e voltada para o futuro. Os benefícios tangíveis desse projeto não só ressoam nos rios agora mais limpos, mas ecoam na qualidade de vida aprimorada, na promoção da sustentabilidade e no legado de uma cidade que escolheu cuidar de seu meio ambiente para as gerações futuras.",
        "comentarios": [],
    },{
        "title": "Uso Responsável da Água",
        "introduction": "A Campanha de Conscientização sobre o Uso Responsável da Água surge como uma resposta proativa a uma das questões mais cruciais da contemporaneidade: a gestão sustentável dos recursos hídricos. Em consonância com a crença de nossa empresa de que a conscientização é o ponto de partida para transformações positivas, essa iniciativa foi concebida com o propósito de educar e engajar a comunidade na preservação responsável da água. Ao longo da campanha, uma série de eventos educacionais, workshops e iniciativas de sensibilização pública foram realizados, todos com o objetivo de destacar a importância da água e fomentar práticas conscientes de uso. A comunidade respondeu de maneira extraordinária, evidenciando uma redução notável no desperdício de água e uma crescente conscientização acerca da necessidade premente de proteger esse recurso vital para as gerações futuras.",
        "paragraph1": "No âmago da campanha, a realização de eventos educacionais proporcionou uma plataforma dinâmica para disseminar conhecimento sobre a importância da água e os impactos do uso irresponsável. Workshops especializados abordaram estratégias práticas para a conservação hídrica, capacitando os participantes a adotarem medidas sustentáveis em suas rotinas diárias. Além disso, iniciativas de sensibilização pública, como campanhas em redes sociais e eventos comunitários, amplificaram a mensagem, gerando uma conscientização abrangente. A notável resposta da comunidade não apenas se refletiu em estatísticas tangíveis de redução no desperdício de água, mas também criou uma cultura local mais atenta à necessidade premente de proteger esse recurso vital. Este projeto exemplifica a eficácia da educação aliada à ação coletiva na promoção de mudanças de comportamento e na construção de um futuro mais sustentável.",
        "paragraph2": "Em síntese, a Campanha de Conscientização sobre o Uso Responsável da Água não apenas atingiu seus objetivos educativos e de sensibilização, mas também moldou positivamente a mentalidade e as práticas da comunidade em relação ao precioso recurso hídrico. A redução significativa no desperdício de água é testemunho claro do impacto direto desta iniciativa. Este projeto não apenas reforça a convicção de que a educação é um catalisador poderoso para a mudança, mas também estabelece um precedente inspirador para outras comunidades, indicando que a união de esforços pode transformar desafios complexos em oportunidades tangíveis para um futuro mais sustentável e equitativo.",
        "conclusion": "Em suma, a Campanha de Conscientização sobre o Uso Responsável da Água representa não apenas um esforço educativo, mas uma jornada coletiva em direção à preservação de nosso recurso mais precioso. Os números refletem uma mudança real no comportamento da comunidade, destacando a eficácia de abordagens inclusivas e educativas. À medida que celebramos a redução no desperdício de água e o aumento da conscientização, também reconhecemos que essa campanha é mais do que um projeto isolado; é um passo significativo em direção a um futuro onde a gestão responsável da água é uma prioridade compartilhada. Este é um legado que transcende os números, influenciando a forma como vivemos e preservamos nosso meio ambiente para as gerações que virão." ,
        "comentarios": [],
    },{
        "title": "Uso Responsável da Água",
        "introduction": "A Campanha de Conscientização sobre o Uso Responsável da Água surge como uma resposta proativa a uma das questões mais cruciais da contemporaneidade: a gestão sustentável dos recursos hídricos. Em consonância com a crença de nossa empresa de que a conscientização é o ponto de partida para transformações positivas, essa iniciativa foi concebida com o propósito de educar e engajar a comunidade na preservação responsável da água. Ao longo da campanha, uma série de eventos educacionais, workshops e iniciativas de sensibilização pública foram realizados, todos com o objetivo de destacar a importância da água e fomentar práticas conscientes de uso. A comunidade respondeu de maneira extraordinária, evidenciando uma redução notável no desperdício de água e uma crescente conscientização acerca da necessidade premente de proteger esse recurso vital para as gerações futuras.",
        "paragraph1": "No âmago da campanha, a realização de eventos educacionais proporcionou uma plataforma dinâmica para disseminar conhecimento sobre a importância da água e os impactos do uso irresponsável. Workshops especializados abordaram estratégias práticas para a conservação hídrica, capacitando os participantes a adotarem medidas sustentáveis em suas rotinas diárias. Além disso, iniciativas de sensibilização pública, como campanhas em redes sociais e eventos comunitários, amplificaram a mensagem, gerando uma conscientização abrangente. A notável resposta da comunidade não apenas se refletiu em estatísticas tangíveis de redução no desperdício de água, mas também criou uma cultura local mais atenta à necessidade premente de proteger esse recurso vital. Este projeto exemplifica a eficácia da educação aliada à ação coletiva na promoção de mudanças de comportamento e na construção de um futuro mais sustentável.",
        "paragraph2": "Em síntese, a Campanha de Conscientização sobre o Uso Responsável da Água não apenas atingiu seus objetivos educativos e de sensibilização, mas também moldou positivamente a mentalidade e as práticas da comunidade em relação ao precioso recurso hídrico. A redução significativa no desperdício de água é testemunho claro do impacto direto desta iniciativa. Este projeto não apenas reforça a convicção de que a educação é um catalisador poderoso para a mudança, mas também estabelece um precedente inspirador para outras comunidades, indicando que a união de esforços pode transformar desafios complexos em oportunidades tangíveis para um futuro mais sustentável e equitativo.",
        "conclusion": "Em suma, a Campanha de Conscientização sobre o Uso Responsável da Água representa não apenas um esforço educativo, mas uma jornada coletiva em direção à preservação de nosso recurso mais precioso. Os números refletem uma mudança real no comportamento da comunidade, destacando a eficácia de abordagens inclusivas e educativas. À medida que celebramos a redução no desperdício de água e o aumento da conscientização, também reconhecemos que essa campanha é mais do que um projeto isolado; é um passo significativo em direção a um futuro onde a gestão responsável da água é uma prioridade compartilhada. Este é um legado que transcende os números, influenciando a forma como vivemos e preservamos nosso meio ambiente para as gerações que virão." ,
        "comentarios": [],
    }
]



@app.route('/paginaProjeto/<index>', methods=['GET'])
def projeto(index):
    return projetos[int(index)]

 


# ... Seu código existente ...

@app.route('/adicionar_comentario', methods=['POST'])
def adicionar_comentario():
    try:
        if request.is_json:
            data = request.get_json()

            print(data)
            
            numero = data.get('numero')
            if numero is None:
                return jsonify({"error": "O campo 'numero' é obrigatório"}), 400
            else:
                numero = int(numero)

            comentario = {
                "nome": data.get('nome'),
                "comentario": data.get('comentario')
            }

            if (numero >= 0 and numero < len(projetos)):
                print("OPa")
                print(numero)
                projeto = projetos[numero]
                projeto["comentarios"].append(comentario)
            else:
                return jsonify({"error": "o numero nao esta dentro da lista de projetos"}), 400

            return jsonify({"message": "Comentário recebido e salvo com sucesso"}), 200
        else:
            return jsonify({"error": "A solicitação deve conter dados JSON"}), 400
    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500


dados_do_formulario_lista=[]

@app.route('/enviarFormulario', methods=['POST'])
def enviarFormulario():
    try:
        dados_do_formulario = request.get_json()
        dados_do_formulario_lista.append(dados_do_formulario)

        print("Lista de dados do formulário:")
        print(dados_do_formulario_lista)

        return jsonify({"message": "Dados do formulário recebidos com sucesso!"}), 200

    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')