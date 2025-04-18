Feature: Target Cart Functionality


  Scenario: Verify "Your cart is empty" message
    Given Open target main page
    When Click on Cart icon
    Then Verify cart is empty message is shown