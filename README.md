# API Avatar

A API Avatar é uma interface de programação de aplicações que permite aos usuários acessar informações sobre o universo da série animada "Avatar: A Lenda de Aang", criada por Michael Dante DiMartino e Bryan Konietzko. Essa API foi desenvolvida em Python e utiliza o formato JSON para a troca de dados.

## Rotas Principais

A API Avatar oferece três rotas principais:

### /base

Retorna informações gerais sobre as quatro nações (Ar, Água, Fogo e Terra) e os personagens principais de cada uma delas, como Aang, Katara, Zuko e Toph. Essas informações incluem detalhes sobre a cultura, geografia, história e política de cada nação, bem como uma lista dos personagens principais associados a cada uma delas.

Exemplo de requisição:
<pre>
  GET /
</pre>


### /dobras

Retorna os tipos de dobras de cada elemento (ar, água, fogo e terra) juntamente com uma breve descrição de suas características e habilidades. Essa rota permite aos usuários explorar as diferentes formas de manipulação dos elementos no universo de Avatar: A Lenda de Aang.

Exemplo de requisição:
<pre>
  GET /dobras
</pre>


### /nacoes

Retorna informações detalhadas sobre as nações e suas províncias. Essa rota fornece descrições aprofundadas sobre as culturas, geografias, histórias e políticas das nações do universo de Avatar: A Lenda de Aang. Os usuários podem usar essa rota para obter um conhecimento mais abrangente sobre cada nação.

Exemplo de requisição:
<pre>
  GET /nacoes
</pre>

# Como usar a API Avatar
Para utilizar a API Avatar, os usuários devem enviar requisições HTTP para a URL base da API, seguida da rota desejada e quaisquer parâmetros opcionais. É possível realizar requisições GET para obter as informações disponíveis em cada rota.

Exemplo de uso da API:
<pre>
  GET http://avatarapi.pythonanywhere.com
</pre>

### Considerações Finais
A API Avatar é uma ferramenta poderosa para os fãs da série "Avatar: A Lenda de Aang" que desejam acessar informações detalhadas sobre o universo e explorar os personagens, as nações e os tipos de dobras apresentados. Esperamos que essa API seja útil e contribua para a experiência dos usuários interessados em aprender mais sobre esse mundo fantástico.

Sinta-se à vontade para contribuir com o projeto e nos fornecer feedback.
