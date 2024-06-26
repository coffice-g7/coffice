// Funcionalidade: Filtrar cafeterias

// Cenário 1:  Apenas um filtro aplicado na filtragem

Given("que estou na página 'home'..", () => {

    cy.visit('http://127.0.0.1:8000/');
    cy.wait(2000);
});

When("seleciono um filtro específico", () => {

    cy.get('.third-line-filters').within(() => {
        cy.get('#VeganFilter').click();
    });
    cy.wait(2000);
});

And("clico em 'Gerar opções'", () => {

    cy.get('.generate-options-button').click();
    cy.wait(2000);
});

And("entro na página de detalhes da cafeteria", () => {

    cy.get('#cards').eq(0).click();

});

Then("devo ver na página da de detalhes da cafeteria o icone correspondente ao filtro escolhido", () => {

    cy.get('#img-vegan').should('be.visible');
    cy.wait(2000);
});



// Cenário 2: Dois filtros aplicados na filtrag

Given("que estou na página 'home'", () => {

    cy.visit('http://127.0.0.1:8000/');
    cy.wait(2000);
});

When("seleciono dois filtros específicos", () => {

    cy.get('.third-line-filters').within(() => {
        cy.get('#ParkingFilter').click();
    });
    cy.get('.third-line-filters').within(() => {
        cy.get('#AcessFilter').click();
    });
    cy.wait(2000);
});

And("clico em 'Gerar opções'", () => {

    cy.get('.generate-options-button').click();
    cy.wait(2000);
});

And("entro na página de detalhes da cafeteria", () => {

    cy.get('#cards').eq(0).click();
    cy.wait(2000);
});

Then("devo ver na página de detalhes da cafeteria os icones correspondentes aos filtros escolhidos", () => {

    cy.get('#img-accessibility').should('be.visible');
    cy.get('#img-parking').should('be.visible');;
    cy.wait(2000);
});