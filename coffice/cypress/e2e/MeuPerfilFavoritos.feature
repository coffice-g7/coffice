#utf-8
#language: pt

Funcionalidade: Manejar Minhas Cafeterias Favoritadas
  Cenário: Visualizar Lista de Cafeterias Favoritas com sucesso
    Dado que tenho um perfil de usuário 
    E eu esteja na página 'home'
    Quando eu favoritar uma cafeteria
    Então essa cafeteria deve ser visualizada na página 'meu perfil' na sessão 'Meus Favoritos'

  Cenário: Remover da Lista uma Cafeteria Favoritada com sucesso
    Dado que tenho um perfil de usuário no site.
    E tenha uma cafeteria favoritada
    Quando eu acessar a minha lista de favoritos
    E remover da minha lista de favoritos
    Então essa cafeteria deve não estar mais presente na lista
