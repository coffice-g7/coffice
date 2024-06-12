// Funcionalidade: Visualizar detalhes da cafeteria

// Cenário 1: Visualizar detalhes da cafeteria com sucesso

Given('que estou na "home"', () => {
    cy.visit('/'); // Visita a página inicial (home)
    cy.url().should('equal', 'http://127.0.0.1:8000/');
    cy.wait(2000); // Espera 2 segundos para garantir que a página carregue completamente
  });
  
  And('existam cafeterias disponíveis', () => {
    cy.get('.card').should('have.length.greaterThan', 0); // Verifica se existem cafeterias (cards) disponíveis
    cy.wait(2000);
  });
  
  When('eu selecionar uma cafeteria', () => {
    cy.get('.card').eq(0).click(); // Seleciona a primeira cafeteria (card) disponível
  });

  Then('devo visualizar seu nome e seus detalhes', () => {
    // Verifica se o nome da cafeteria é visível e não vazio
    cy.get('#NomeCafeteria').should('be.visible').and('not.be.empty');
    cy.wait(2000);
    // Verifica se o endereço da cafeteria é visível e não vazio
    cy.get('.box-name h2').should('be.visible').and('not.be.empty');
  
    // Verifica se a descrição da cafeteria é visível e não vazia
    cy.get('#DescricaoCafeteria').should('be.visible').and('not.be.empty');
  
    // Verifica se as avaliações (estrelas) são visíveis e se há pelo menos uma estrela
    cy.get('#CaixaNotas .star-icon').should('be.visible').and('have.length.greaterThan', 0);
    cy.wait(2000);
    // Verifica se a pontuação da cafeteria é visível
    cy.get('.box-ratings span').should('be.visible').and('not.be.empty');
  
    cy.wait(2000);
    // Verifica se o link para mais avaliações é visível e não vazio
    cy.get('.avaliacoes-button-link').should('be.visible').and('not.be.empty');
  });
  