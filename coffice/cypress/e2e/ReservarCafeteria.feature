#utf-8
#language: pt

Funcionalidade: Reservar Cafeteria
 Dado que tenho um perfil de usuário no site
    E eu esteja na página 'home'
    Quando eu reservar uma cafeteria específica
    Então essa cafeteria deve ser visualizada no painel de "Minhas Reservas" no "Meu Perfil"

  Cenário: Cancelar reservas com sucesso
    Dado que tenho um perfil de usuário registrado no site
    E uma cafeteria específica está marcada como pendente na minha lista de "Minhas Reservas"
    Quando eu clicar em "cancelar"
    Então deve ser exibida abaixo a mensagem "cancelada"
