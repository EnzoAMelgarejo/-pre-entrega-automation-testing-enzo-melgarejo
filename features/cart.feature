@ui
Feature: Funcionalidad de carrito en SauceDemo

  Background:
    Given que el usuario inicia sesion con standard_user

  @regression
  Scenario: Agregar un producto al carrito
    When el usuario agrega el producto "Sauce Labs Backpack" al carrito
    Then el contador del carrito debe ser "1"

  @regression
  Scenario Outline: Agregar multiples productos al carrito
    When el usuario agrega el producto "<producto>" al carrito
    Then el producto "<producto>" debe estar en el carrito

    Examples:
      | producto              |
      | Sauce Labs Backpack   |
      | Sauce Labs Bike Light |
      | Sauce Labs Bolt T-Shirt |