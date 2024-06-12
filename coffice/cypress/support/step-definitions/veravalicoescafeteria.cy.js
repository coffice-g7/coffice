// Funcionalidade: Visualizar Avaliações de Cafeteria

// Cenário 1: Visualizar Avaliações de Cafeteria com sucesso

Given('que estou logado no sistema como usuário cliente;', () => {
    cy.visit('/register');
    cy.cadastrar('testeavaliacao', 'tst@cesar.school', '92£*B3>N.Ut8', '12345698922', '12345678', '123');
});

And('estou na página de detalhes de uma cafeteria específica', () => {
    cy.get('#cards').eq(0).click(); 
    cy.wait(2000);
});

When('eu visualizar a seção de avaliações', () => {
    cy.get('#btnavaliar').click(); 
    cy.wait(2000);
});

Then('devo ver uma lista de avaliações de outros usuários para essa cafeteria', () => {
    cy.get("#reviewcard").should('be.visible'); 
    cy.wait(2000);
});

And('as avaliações devem incluir a nota e o comentário de cada usuário', () => {
    cy.get("#reviewid").should('exist'); 
    cy.wait(2000);
});