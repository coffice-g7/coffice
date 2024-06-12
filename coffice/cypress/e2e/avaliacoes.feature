#utf-8
#language: pt

Funcionalidade: Ver avaliações
    Cenário: visualizar avaliações de uma cafeteria
    Dado que estou logado no sistema como usuário cliente;
    E estou na página de detalhes de uma cafeteria específica
    Quando eu visualizar a seção de avaliações
    Então devo ver uma lista de avaliações de outros usuários para essa cafeteria
    E as avaliações devem incluir a nota e o comentário de cada usuário