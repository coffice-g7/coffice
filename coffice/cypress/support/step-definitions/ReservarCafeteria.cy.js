// Funcionalidade: Reservar Cafeteria

Given('que tenho um perfil de usuário no site.;', function () {
    cy.visit('/register');
    cy.cadastrar('testeres3', 'tst3@cesar.school', '92£*B3>N.Ut8', '12345698922', '12345678', '123');
});

And("eu esteja na página 'home'", function () {
    cy.url().should('equal', 'http://127.0.0.1:8000/');
    cy.wait(2000);
});

var reservationDate = '2024-06-13T10:00';

When("eu reservar uma cafeteria específica", function () {
    cy.get('#cards').should('have.length.greaterThan', 0); // Verifica se existem cafeterias (cards) disponíveis
    cy.get('#cards').eq(0).click(); // Seleciona a primeira cafeteria (card) disponível
    cy.get(':nth-child(1) > .avaliacoes-button-2-link').click(); // Clica no botão para fazer reserva
    // Preenche os campos do formulário
    cy.get('input[name="name"]').type('Thiago Souls');
    cy.get('input[name="date"]').type(reservationDate);
    cy.get('input[name="num_people"]').type('2');
    cy.get('input[name="duration"]').type('60');
    cy.wait(2000);
    cy.get('form').submit();

});

Then('essa cafeteria deve ser visualizada no painel de "Minhas Reservas" no "Meu Perfil"', function () {
    // Verifica se a reserva foi feita com sucesso
    cy.contains('Minhas Reservas').click();
    
    cy.get('.reservation-card').eq(0).within(() => {
        const formattedDate = formatDateForUI(reservationDate);

        cy.get('.reservation-card-date').should('contain.text', formattedDate.trim());
    });
    cy.wait(2000);

});

function formatDateForUI(dateString) {
    const options = { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' };
    const date = new Date(dateString);
    const day = date.toLocaleDateString('pt-BR', { day: '2-digit' });
    const month = date.toLocaleDateString('pt-BR', { month: 'short' }).replace('.', '');
    const capitalizedMonth = month.charAt(0).toUpperCase() + month.slice(1);
    const time = date.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });

    return `${day} de ${capitalizedMonth}, ${time}`;
}


