#utf-8
#language: pt

Funcionalidade: Visualizar detalhes da cafeteria
  Cenário: Visualizar detalhes da cafeteria com sucesso
    Dado que estou na "home"
    E existam cafeterias disponíveis
    Quando eu selecionar uma cafeteria
    Então devo visualizar seu nome e seus detalhes
