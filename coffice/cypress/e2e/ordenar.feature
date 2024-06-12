#utf-8
#language: pt

Funcionalidade: Ordenar as avaliações de uma cafeteria.
    
    Cenário: Ordenar por mais relevante
    Dado que estou logado no sistema como usuário cliente
    E estou na página de detalhes de uma cafeteria específica
    Quando eu visualizar a seção de avaliações
    E selecionar a opção "Mais Relevantes" para ordenar as avaliações
    Então as avaliações devem ser exibidas na ordem mais relevante

    Cenário: Ordenar por mais recente
    Dado que estou logado no sistema com usuário cliente
    E estou na página de detalhes de uma cafeteria específica
    Quando eu visualizar a seção de avaliações
    E selecionar a opção "Mais Recentes" para ordenar as avaliações
    Então as avaliações devem ser exibidas na ordem mais recente