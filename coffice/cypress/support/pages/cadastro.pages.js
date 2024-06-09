const INPUT_NOME = '#username'
const INPUT_EMAIL = '#email'
const INPUT_SENHA = '#password1'
const INPUT_CONFIRMAR_SENHA = '#password2'
const INPUT_CPF = '#cpf'
const INPUT_ZIP_CODE = '#cep'
const INPUT_NUMBER = '#number'
const BUTTON_TERMS = '#checkmarkbox' 
const BUTTON_SUBMIT = '#registerButton' 


Cypress.Commands.add('cadastrar', (nome, email, senha, cpf,  cep, numero) => {
    cy.get(INPUT_NOME).type(nome)
    cy.get(INPUT_CPF).type(cpf)
    cy.get(INPUT_EMAIL).type(email)
    cy.get(INPUT_SENHA).type(senha)
    cy.get(INPUT_CONFIRMAR_SENHA).type(senha)
    cy.get(INPUT_ZIP_CODE).type(cep)
    cy.get(INPUT_NUMBER).type(numero)
    cy.get(BUTTON_TERMS).click()
    cy.get(BUTTON_SUBMIT).click()
})