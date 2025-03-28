# Created by joshzz at 3/28/25
Feature: Add product to the cart and verify total price

  Scenario: User adds a product to the cart and verifies the total price
    Given User is on the Target homepage
    When User searches for a product "Laptop"
    And User adds the product to the cart
    And User navigates to the cart
    Then The total price of the cart should be greater than 0