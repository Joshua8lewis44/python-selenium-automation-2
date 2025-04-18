Feature: Target search test cases

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results shown for <expected_text>
    Examples:
    |search_word  |expected_text  |
    |tea          |tea            |
    |iPhone       |iPhone         |
    |dress        |dress          |

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product