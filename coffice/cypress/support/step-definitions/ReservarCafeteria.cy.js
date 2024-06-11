// Funcionalidade: Reservar Cafeteria

describe('Reservar Cafeteria', () => {
    beforeEach(() => {
        // Antes de cada teste, registra um novo usuário
        cy.visit('/register');
        cy.cadastrar('testereg', 'tcq@cesar.school', '92£*B3>N.Ut8', '12345698900', '12345678', '123');
    });

    it('Deve reservar uma cafeteria específica com sucesso', () => {
        // Realiza a reserva em uma cafeteria específica
        cy.visit('/');
        cy.visit('/coffee_shop/1/');
        cy.visit('/make/1/');
        
        // Preenche os campos do formulário
        cy.get('input[name="date"]').type('2024-06-11T10:00');
        cy.get('input[name="num_people"]').type('2');
        cy.get('input[name="duration"]').type('60');
        cy.get('form').submit();
    
        // Verifica se a reserva foi feita com sucesso
        cy.contains('Minhas Reservas').click();
        cy.contains('Cafeteria da Lulu').should('exist');
    });

    it('Deve cancelar uma reserva com sucesso', () => {
        // Realiza o login com o usuário registrado
        cy.visit('/login');
        cy.realizarLogin('testereg', '123');
        
        // Realiza a reserva em uma cafeteria específica
        cy.visit('/coffee_shop/1/');
        cy.visit('/make/1/');
        
        // Preenche os campos do formulário
        cy.get('input[name="date"]').type('2024-06-11T10:00');
        cy.get('input[name="num_people"]').type('2');
        cy.get('input[name="duration"]').type('60');
        cy.get('form').submit();
    
        // Verifica se a reserva foi feita com sucesso
        cy.contains('Minhas Reservas').click();
        cy.contains('Nome da Cafeteria').should('exist');
        
        // Clica em "Cancelar" para cancelar a reserva
        cy.contains('Cancelar').click();
    
        // Verifica se a reserva foi cancelada com sucesso
        cy.contains('cancelada').should('exist');
        
        // Volta para "Minhas Reservas"
        cy.go('back');
        // ou
        // cy.contains('Minhas Reservas').click(); // Se houver um botão/link para "Minhas Reservas"
    });
});
