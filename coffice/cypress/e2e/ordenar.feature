#utf-8
#language: pt

Funcionalidade:  ordernar as avaliações de uma cafeteria.
    Cenário: Ordenar avaliações com sucesso
    Dado que estou logado no sistema como usuário cliente
    E estou na página de detalhes de uma cafeteria específica
    Quando eu visualizar a seção de avaliações
    E selecionar uma opção para ordenar as avaliações
    Então as avaliações devem ser exibidas na ordem selecionada