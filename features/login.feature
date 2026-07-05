@ui
Feature: Autenticacion de usuarios en SauceDemo

  Background:
    Given que el usuario abre la pagina de login

  @smoke
  Scenario: Login exitoso con credenciales validas
    When el usuario ingresa el usuario "standard_user" y la clave "secret_sauce"
    Then debe ser redirigido al inventario

  Scenario Outline: Login fallido con credenciales invalidas
    When el usuario ingresa el usuario "<usuario>" y la clave "<clave>"
    Then debe ver un mensaje de error visible

    Examples:
      | usuario         | clave             |
      | standard_user   | clave_incorrecta  |
      | locked_out_user | secret_sauce      |
      |                 |                   |