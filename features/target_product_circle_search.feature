Feature: Verify benefits on the Target Circle page

  Scenario: User verifies there are at least 10 benefit cells
    Given User is on the Target Circle page
    Then There should be at least 10 benefit cells on the page