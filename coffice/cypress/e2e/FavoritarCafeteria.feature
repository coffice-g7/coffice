#utf-8
#language: pt

Funcionalidade: Favoritar Cafeteria
  Cenário: Favoritar Cafeteria com sucesso
    Dado que tenho um perfil de usuário no site
    E eu esteja na página 'home'
    Quando eu favoritar uma cafeteria específica
    Então essa cafeteria deve ser visualizada com prioridade e como favorita no painel de cafeterias

  Cenário: Desfavoritar uma cafeteria com sucesso
    Dado que tenho um perfil de usuário registrado no site
    E uma cafeteria específica está marcada como favorita na minha lista
    Quando eu clicar em favoritar e clicar novamente para desfavoritar 
    Então deve ser removida o favorito da cafeteria
