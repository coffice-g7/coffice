#utf-8
#language: pt

Funcionalidade: Reservar Cafeteria
  Cenário: Reservar Cafeteria com sucesso 
    Dado que tenho um perfil de usuário no site
    E eu esteja na página 'home'
    Quando eu reservar uma cafeteria específica
    Então essa cafeteria deve ser visualizada no painel de "Minhas Reservas" no "Meu Perfil"

