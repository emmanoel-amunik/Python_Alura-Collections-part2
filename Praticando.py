from collections import Counter


text1 = """
Na última década as mídias sociais deixaram de ser um passatempo e 
se tornaram parte do nosso dia a dia, a ponto de mais de 60% da população 
global estar presente nelas. A força dessas plataformas é tão grande que 
elas influenciam diversos aspectos das nossas vidas e, entre coisas, 
transformaram a maneira como consumimos conteúdo online e fizeram com que a 
comunicação fosse hoje muito mais visual do que antes, tornando os vídeos 
uma ferramenta essencial nesse sentido.

Portanto, o acabamento desses materiais é fundamental para a criação de 
peças de comunicação visual efetivas. Neste artigo vamos discutir as cinco 
melhores práticas para edição de vídeos voltados para mídias sociais, 
sendo elas:

Muitos vídeos são reproduzidos automaticamente nas redes sociais e muitas 
vezes eles se reproduzem sem som. Garanta uma abertura visualmente atrativa 
que transmita a essência do vídeo sem depender do áudio. Imagens impactantes 
e gráficos envolventes podem ser cruciais nos primeiros segundos.

Integre elementos gráficos e animações para tornar o vídeo mais dinâmico. 
Isso não apenas aumenta o apelo visual, mas também pode ser usado para 
destacar informações importantes. Evite excessos para não sobrecarregar o 
espectador.
"""


text2 = """
O universo das vendas e do marketing é um mar cheio de 
possibilidades e desafios. Para se destacar nesse ambiente, não basta apenas 
ter um bom produto ou serviço; é essencial dominar certas técnicas que 
transformam a maneira como interagimos e nos conectamos com nosso público.

Neste artigo, vamos mergulhar em três estratégias poderosas que podem ser 
verdadeiros faróis para qualquer profissional da área:

Em marketing e vendas, entender bem quem é seu público é essencial. Essa 
estratégia envolve conhecer o cliente ideal, para que as ações sejam 
realmente eficazes. O segredo está em ajustar as mensagens para atender 
exatamente o que o público quer e precisa, em vez de usar uma abordagem 
muito geral, o que muitas vezes não dá certo.

Para ajudar nisso, a ferramenta de criação de persona foi desenvolvida. Uma 
persona é uma representação semi-fictícia do cliente ideal de um negócio, 
baseada em dados reais sobre comportamentos e características demográficas 
de clientes existentes.

Essa ideia foi criada por Alan Cooper nos anos 80. Ele é um designer de 
software que desenvolveu a ideia, destacando a importância de entender os 
usuários finais e projetar sistemas que atendam às suas necessidades e 
expectativas.

Assim, a criação de personas envolve a definição de perfis detalhados que 
incluem informações como idade, sexo, localização geográfica, interesses, 
comportamentos de compra, desafios e objetivos. O objetivo é ter uma 
compreensão mais profunda dos clientes para que as estratégias de marketing, 
vendas e desenvolvimento de produtos possam ser personalizadas de acordo.

Uma boa persona detalha o que a pessoa gosta, o que busca, o que valoriza e 
quais são seus desafios. É uma forma de entender melhor o cliente, não só 
quem ele é, mas o que o motiva.

Por exemplo, se uma empresa vende produtos ou serviços para profissionais de 
marketing digital, poderia criar personas como "Ana, a Analista de Mídias 
Sociais" ou "Carlos, o Gerente de SEO". 
"""


def character_frequency_analyser(text):
    appearances = Counter(text.lower())
    total_characters = sum(appearances.values())

    proportions = [(letter, frequency / total_characters) for letter, frequency
                   in appearances.items()]
    proportions = Counter(dict(proportions))

    for character, proportion in proportions.most_common():
        print(f"'{character}' - {proportion * 100:.2f}%")


print(character_frequency_analyser(text1))
print("============")
print(character_frequency_analyser(text2))
