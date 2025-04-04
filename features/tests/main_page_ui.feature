Feature: Search and Cart functionality on Target website

  Scenario Outline: Search for a product and view cart
    Given I am on the Target website
    When I search for "<product>"
    Then I should see search results for "<product>"
    When I click on the cart icon
    Then I should be taken to the cart page

  Examples:
    | product   |
    | iPhone    |
    | MacBook   |
    | AirPods   |