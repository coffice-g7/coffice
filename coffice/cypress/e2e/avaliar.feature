#utf-8
#language: pt

Funcionalidade: Avaliar uma cafeteria
    Cenário: Avaliar uma cafeteria com sucesso
    Dado que estou logado no sistema como usuário cliente
    E estou na página de detalhes de uma cafeteria
    Quando eu visualizar a seção de avaliações
    E clicar no botão para adicionar uma nova avaliação
    Então devo ver um formulário para inserir minha avaliação
    E após submeter o formulário com sucesso
    Então a avaliação deve ser exibida na página da cafeteria