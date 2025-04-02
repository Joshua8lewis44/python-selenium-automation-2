
Feature: Sign In navigation on Target.com

  Scenario: Verify that a logged-out user can navigate to the Sign In page
    Given I am on the Target homepage
    When I click on the "Sign In" link in the navigation menu
    And I click the "Sign In" option from the right-side navigation menu
    Then I should see the Sign In form