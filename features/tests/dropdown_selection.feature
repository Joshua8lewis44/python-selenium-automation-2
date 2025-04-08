Feature: Verify Dropdown Selection on Target Help page

  Scenario: Select a different topic from the dropdown menu and verify correct page
    Given I navigate to the Target Help page
    When I select "Returns & Exchanges" from the dropdown menu
    Then I should be redirected to the correct page for "Returns & Exchanges"

  Scenario: Select another topic from the dropdown menu and verify correct page
    Given I navigate to the Target Help page
    When I select "Promotions & Coupons" from the dropdown menu
    Then I should be redirected to the correct page for "Promotions & Coupons"
