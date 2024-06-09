// Funcionalidade: Favoritar Cafeteria

// Cenário 1:  Favoritar Cafeteria com sucesso

Given('que tenho um perfil de usuário no site', () => {
    cy.visit('/register');
    cy.cadastrar('testefav1', 'tst@cesar.school', '92£*B3>N.Ut8', '12345698900', '12345678', '123');
  });
  
  And("eu esteja na página 'home'", () => {
    cy.url().should('equal', 'http://127.0.0.1:8000/');
    cy.wait(2000);
  });
  
  When('eu favoritar uma cafeteria específica', () => {
    cy.get('.card').eq(1).within(() => {
      cy.get('#Nao-favoritado').click(); 
    });
  });
  
  Then('essa cafeteria deve ser visualizada com prioridade e como favorita no painel de cafeterias', () => {
    cy.get('.card').first().within(() => {
      cy.get('#favoritado').should('be.visible'); 
    });
  });
  

  // Cenário 2: Desfavoritar uma cafeteria com sucesso

Given('que tenho um perfil de usuário registrado no site', () => {
    cy.visit('/register');
    cy.cadastrar('testefav2', 'tt2@cesar.school', '92£*B3>N.Ut8', '12345698911', '12345678', '123');
  });
  
  And('uma cafeteria específica está marcada como favorita na minha lista', () => {
    cy.wait(2000);
    cy.get('.card').first().within(() => {
      cy.get('#Nao-favoritado').click(); 
    });
    cy.get('.card').first().within(() => {
      cy.get('#favoritado').should('be.visible'); 
    });
  });
  
  When('eu clicar em favoritar e clicar novamente para desfavoritar', () => {
    cy.get('.card').first().within(() => {
      cy.get('#favoritado').click(); 
    });
  });
  
  Then('deve ser removida o favorito da cafeteria', () => {
    cy.get('.card').first().within(() => {
      cy.get('#Nao-favoritado').should('be.visible'); 
    });
  });
  