#HW_3: Created by Andy K Piri at 10/25/2022
Feature: Amazon Sign In
  Scenario: Verify that User is able to see the 'Sign-In' page when clicking on 'Orders' button
    Given Open the Amazon Page
    And Click on Orders button
    Then Sign in page opened: Sign In header is visible, email input field is present.


  Scenario: Verify that User sees a message that  "Your Amazon Cart is empty".
    Given Open the Amazon Page
    And Click on the Cart icon
    Then Verify that "Your Amazon Cart is empty" message is displayed



  Scenario: Verify that User is able to see there are '5 links' when clicking on 'Amazon Best Sellers' button
    Given Open the Amazon Bestseller  Page
    Then Verify that user is able to see 5 links