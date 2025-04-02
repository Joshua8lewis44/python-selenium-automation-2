Feature: Target search test cases

  Scenario: Verify that "Your cart is empty" message is shown when the cart icon is clicked
    Given I am on the Target homepage
    When I click on the cart icon
    Then I should see the "Your cart is empty" message