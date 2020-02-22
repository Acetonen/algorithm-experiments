Feature: Get length of link
  In order to to find length of linked list
  We'll implement len() method

  Scenario Outline: Find the length of list
    Given I have list as <list_of_numbers>
    When I call .len method
    Then I see the number of nodes in list as <length>

    Examples:
      | list_of_numbers | length |
      | 1 2 3           | 3      |
      |                 | 0      |