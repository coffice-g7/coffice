#utf-8
#language: pt

Funcionalidade: Filtrar cafeterias
  Cenário: Apenas um filtro aplicado na filtragem
    Dado que estou na página 'home'..
    Quando seleciono um filtro específico
    E clico em 'Gerar opções'
    E entro na página de detalhes da cafeteria
    Então devo ver na página da de detalhes da cafeteria o icone correspondente ao filtro escolhido

  Cenário: Dois filtros aplicados na filtragem
    Dado que estou na página 'home'
    Quando seleciono dois filtros específicos
    E clico em 'Gerar opções'
    E entro na página de detalhes da cafeteria
    Então devo ver na página de detalhes da cafeteria os icones correspondentes aos filtros escolhidos
