// Funcionalidade: Ordenar Avaliações de uma Cafeteria

// Cenário: Ordenar por mais relevante

Given('que estou logado no sistema como usuário cliente', () => {
    cy.visit('/register');
    cy.cadastrar('testeordenar', 'tst@cesar.school', '92£*B3>N.Ut8', '12345698922', '12345678', '123');
});
  
And('estou na página de detalhes de uma cafeteria específica', () => {
    cy.get('.card').eq(0).click(); 
});
  
When('eu visualizar a seção de avaliações', () => {
    cy.get('#btnavaliar').click(); 
});
  
And('selecionar a opção "Mais Relevantes" para ordenar as avaliações', () => {
    cy.get("#ordenar1").click();
});
  
Then('as avaliações devem ser exibidas na ordem mais relevante', () => {
    cy.get("#reviewid").should('exist');
});

// Cenário: Ordenar por mais recente

Given('que estou logado no sistema com usuário cliente', () => {
    cy.visit('/login');
    cy.login('tst@cesar.school', '92£*B3>N.Ut8');
});
  
And('estou na página de detalhes de uma cafeteria específica', () => {
    cy.wait(2000);
    cy.get('.card').eq(0).click(); 
});
  
When('eu visualizar a seção de avaliações', () => {
    cy.get('#btnavaliar').click(); 
});
  
And('selecionar a opção "Mais Recentes" para ordenar as avaliações', () => {
    cy.get("#ordenar2").click();
});
  
Then('as avaliações devem ser exibidas na ordem mais recente', () => {
    cy.get("#reviewid").should('exist');
});