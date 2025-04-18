Feature: Target Sign In Navigation

  Scenario: Logged out user can navigate to Sign In
    Given Open target main page
    When Click on Sign In
    And Click Sign In from side menu
    Then Verify Sign In form is shown
