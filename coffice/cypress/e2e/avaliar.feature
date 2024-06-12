#utf-8
#language: pt

Funcionalidade: Avaliar uma cafeteria
  Cenário: Avaliar uma cafeteria com sucesso
    Dado que tenho um cadastro no sistema como usuário cliente...
    E tenha cafeterias existentes na home
    E estou na página de detalhes da cafeteria..
    Quando eu visualizar a seção de avaliações..
    E submeter o formulário de avaliação
    Entao deve haver ao menos uma avaliação a ser exibida na página da cafeteria