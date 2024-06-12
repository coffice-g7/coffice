Cypress.Commands.add('criarCards', (Nome, mensagem) => {
    cy.visit('/admin/base/coffee_shop/add/');
    
    // Preenche os campos do formulário
    cy.get('#id_name').type(Nome);
    cy.get('#id_email').type('email@cafemail.com');
    cy.get('#id_description').type(mensagem);
    // Fill out other fields as needed...
    cy.get('#id_rating').type('4');
    cy.get('#id_has_silent_environment').check();
    cy.get('#id_cnpj').type('12345678901234');
    cy.get('#id_allow_reservation').check();
    cy.get('#id_reservation_cost').type('10.00');
    cy.get('#id_coffee_spotlight').type('Destaque do café');
    cy.get('#id_allow_reservation').check();
    cy.get('#id_reservation_cost').type('10.00');
    cy.get('#id_coffee_spotlight').type('Destaque do café');
    cy.get('#id_internet_speed').type('100');
    cy.get('#id_vegan_options').check();
    cy.get('#id_zero_lactose_options').check();
    cy.get('#id_gluten_free_options').check();
    cy.get('#id_accessibility').check();
    cy.get('#id_has_parking').check();
    cy.get('#id_has_meeting_room').check();
    cy.get('#id_street').type('Rua do Café');
    cy.get('#id_neighborhood').type('Bairro do Café');
    cy.get('#id_zip_code').type('12345-678');
    cy.get('#id_phone').type('(99) 9999-9999');
    cy.get('#id_instagram').type('@cafedoinstagram');
    cy.get('#id_site_url').type('https://coffice.com.br');
    cy.get('#id_alone').check();

    // Submete o formulário
    cy.get('input[name="_save"]').click();
    
    // Verifica se a entrada de feedback foi criada com sucesso
    cy.url().should('contain', '/admin/base/coffee_shop/');
    cy.contains(Nome).should('exist');
    // Check for other fields or messages to ensure success...

    // Volta para a página inicial do site
    cy.visit('/');
});
