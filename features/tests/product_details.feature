Feature: Test color selection on Target product pages

  Scenario Outline: User can select and verify colors for a product
    Given I open the target product "<product_id>" page
    Then I should be able to click through the color options and verify the selected color

  Examples:
    | product_id  |
    | A-91511634  |
    | A-54511690  |