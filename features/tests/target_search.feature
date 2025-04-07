Scenario: User can add a product to cart
    Given I am on the Target website
    When I search for "mug"
    And I click on the "Add to Cart" button
    And I store the product name
    And I confirm the Add to Cart button in the side navigation
    And I open the cart page
    Then I verify the cart has 1 item(s)
    And I verify the cart has the correct product