Feature: Tests for Target App page

  @smoke
  Scenario: User can open and close Terms and Conditions from sign-in page
    Given Open Target App page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page opened
    And Close current page
    And Return to original windowbehave
