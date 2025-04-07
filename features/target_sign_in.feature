Feature: User can access Sign In page

  Scenario: User can access Sign In from the header
    Given Open target main page
    When Click Sign In on header
    Then Verify Sign In form opened

  Scenario: User can access Sign In from the right-side navigation menu
    Given Open target main page
    When Click Sign In from navigation menu
    Then Verify Sign In form opened