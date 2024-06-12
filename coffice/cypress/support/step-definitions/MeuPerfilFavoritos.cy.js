
// Funcionalidade: Visualizar Lista de Cafeterias Favoritas

// Cenário 1: Visualizar Lista de Cafeterias Favoritas com sucesso

Given('que tenho um perfil de usuário', function() {
    cy.visit('/register');
    cy.cadastrar('testefav3', 'tst3@cesar.school', '92£*B3>N.Ut8', '12345698922', '12345678', '123');
});

And("eu esteja na página 'home'", function() {
    cy.url().should('equal', 'http://127.0.0.1:8000/');
    cy.wait(2000);
});

When('eu favoritar uma cafeteria', function() {
    // Armazena o nome da cafeteria favoritada em uma variável
    cy.get('.card').eq(1).within(() => {
        cy.get('.title-text').invoke('text').then((text) => {
            this.favoritedCoffeeName = text.trim();
        });
        cy.wait(2000);
        cy.get('#Nao-favoritado').click(); 
    });
    cy.wait(2000);
});

Then("essa cafeteria deve ser visualizada na página 'meu perfil' na sessão 'Meus Favoritos'", function() {
    cy.visit('/myprofile');
    cy.get('#favoritos-tab').click();
    cy.get('#favoritos-content').within(() => {
        // Verifica se o nome da cafeteria favoritada bate com o que está lá
        cy.get('.card').eq(0).within(() => {
            cy.wait(2000);
            cy.get('#NomeCafeteria').should('have.text', this.favoritedCoffeeName);
        });
    });
});


// Cenário 2: Remover da Lista uma Cafeteria Favoritada com sucesso

// Dado que tenho um perfil de usuário registrado no site
Given('que tenho um perfil de usuário no site.', () => {
    cy.visit('/register');
    cy.cadastrar('testefav4', 'tst4@cesar.school', '92£*B3>N.Ut8', '12345698933', '12345678', '123');
});

// E tenha uma cafeteria favoritada
And('tenha uma cafeteria favoritada', function() {
    cy.wait(2000);
    cy.get('.card').eq(1).within(() => {
        cy.get('.title-text').invoke('text').then((text) => {
            this.favoritedCoffeeName = text.trim();
        });
        cy.wait(2000);
        cy.get('#Nao-favoritado').click();
    });
});

// Quando eu acessar a minha lista de favoritos
When('eu acessar a minha lista de favoritos', () => {
    cy.visit('/myprofile');
    cy.get('#favoritos-tab').click();
    cy.wait(2000);
});

// E remover da minha lista de favoritos
And('remover da minha lista de favoritos', () => {
    cy.get('.card').eq(0).within(() => {
        cy.wait(2000);
        cy.get('#FavSuccess').click(); 
    });
});

// Então essa cafeteria deve não estar mais presente na lista
Then('essa cafeteria deve não estar mais presente na lista', function() {
    cy.get('#favoritos-content .card').should('not.exist');
});