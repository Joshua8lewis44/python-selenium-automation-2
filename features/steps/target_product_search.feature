# Created by joshzz at 3/28/25
Feature: Target product search

  Scenario: User searches for a product and sees search results
    Given User is on the Target homepage
    When User searches for a product "Laptop"
    Then Results for "Laptop" should be displayed