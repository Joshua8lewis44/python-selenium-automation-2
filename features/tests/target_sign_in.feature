Feature: Target Sign-In page functionality

  Scenario: User enters correct email, incorrect password, and sees an error message
    Given I navigate to the Target sign-in page
    When I enter the correct email and click Continue
    And I enter the incorrect password and click Sign In
    Then I should see an error message indicating invalid password