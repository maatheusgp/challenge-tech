# challenge-tech

###Desafio time de dados tratados

###Objetivo desse repositório

O desafio
Nosso time fictício está interessado em investigar a relevância dos contratos inteligentes
Ethereum no mercado, principalmente para conseguir se mover rápido caso ocorra um pico na
adoção dos mesmos.
Os dados de contratos inteligentes estão disponíveis em um dataset público e gratuito da
Google. Este dataset fica dentro do BigQuery, banco de dados voltado para analytics, no
seguinte endereço:

- Projeto: “bigquery-public-data”
- Dataset: “crypto_ethereum”

Para acessar estes dados você precisará criar uma conta gratuita na Google Cloud Platform
(GCP) onde é disponibilizado 1TB de consultas gratuitamente todo mês. Como os dados de
contratos inteligentes tem em torno de 30MB isso deveria ser o suficiente.
Gostaríamos de montar algumas tabelas tratadas para acompanharmos o crescimento e
relevância dos contratos em relação ao tempo. Precisamos que esse processo seja 100%
server side, não podemos ter processos rodando na máquina dos nossos desenvolvedores.

Perguntas que gostaríamos de responder com nossa(s) tabela(s):
- Quantos contratos (tokens) estão sendo criados por bloco?
- Quantos blocos estão sendo criados em um dia?
- Em relação aos últimos 15 dias, qual foi a variação na quantidade de blocos contendo
tokens em um dia?
- Qual o bloco que gerou contratos (tokens) e utilizou mais taxa (gas)? Informar o nome
de todos os tokens contidos neste bloco

Para a execução diária do código que criará as tabelas, você pode utilizar qualquer solução,
desde que seja server side. Caso não consiga encontrar uma solução para executar as
consultas diariamente, você pode versionar o SQL que responde a(s) pergunta(s) e explicar na
hora de apresentar o desafio.
Critérios de conclusão do desafio

- Para que possamos considerar o desafio entregue, precisamos que você disponibilize o
código em algum serviço de git (ex.: Github, Gitlab, Bitbucket, etc) público ou privado
(dando acesso aos revisores). Não serão considerados commits após a data de entrega
do desafio;
