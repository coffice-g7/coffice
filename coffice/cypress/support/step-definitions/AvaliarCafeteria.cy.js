Given('que tenho um cadastro no sistema como usuário cliente...', () => {
    cy.visit('/register');
    cy.cadastrar('testeAva1', 'tst@cesar.school', '92£*B3>N.Ut8', '12345698900', '12345678', '123');
    });
    
    And('tenha cafeterias existentes na home', () => {
    cy.get('#cards').should('have.length.greaterThan', 0); // Verifica se existem cafeterias (cards) disponíveis
    });

    And("estou na página de detalhes da cafeteria..", () => {
    cy.get('#cards').eq(0).click();
    cy.wait(2000);
    });
    
    When('eu visualizar a seção de avaliações..', () => {
    cy.wait(2000);
    cy.get('#AvaliarCafetria').should('be.visible');
    cy.get('#AvaliarCafetria').click(); 

    });
    
    And('submeter o formulário de avaliação', () => {
    
cy.get('#foodRating .star').each(($el, index) => {
    if (index < 3) { // Seleciona 3 estrelas, por exemplo
    cy.wrap($el).click();
    }
});

// Selecionar estrelas para "Bebida"
cy.get('#drinkRating .star-2').each(($el, index) => {
    if (index < 4) { // Seleciona 4 estrelas, por exemplo
    cy.wrap($el).click();
    }
});

// Selecionar estrelas para "Ambiente"
cy.get('#ambianceRating .star-3').each(($el, index) => {
    if (index < 2) { // Seleciona 2 estrelas, por exemplo
    cy.wrap($el).click();
    }
});

// Selecionar estrelas para "Geral"
cy.get('#overallRating .star-4').each(($el, index) => {
    if (index < 5) { // Seleciona 5 estrelas, por exemplo
    cy.wrap($el).click();
    }
});

// Escrever uma mensagem no campo de comentário
cy.get('.comment-field textarea').type('Excelente lugar, adorei a comida e a bebida!');

// Enviar o formulário
cy.wait(2000);
cy.get('form').submit();
    });


Then('deve haver ao menos uma avaliação a ser exibida na página da cafeteria', () => {
cy.get('#reviewcard').should('be.visible');
cy.wait(2000);
});