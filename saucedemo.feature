Feature: Saucedemo Webpage Validation



  Scenario: 1 Successful Login
    Given I am on the Demo Login Page
    When I fill the account information for account StandardUser into the Username field and the Password field
    And I click the Login Button
    Then I am redirected to the Demo Main Page
    And I verify the App Logo exists

  Scenario: 2 Failed Login
      Given I am on the Demo Login Page
      When I fill the account information for account LockedOutUser into the Username field and the Password field
      And I click the Login Button
      Then I verify the Error Message contains the text "Sorry, this user has been banned."

  Scenario: 3 Order a Product
      Given I am on the Demo Login Page
      When I fill the account information for account StandardUser into the Username field and the Password field
      And I click the Login Button
      Given I am on the inventory Page
      When user sorts products from low price to high price
      And user adds lowest priced product
      And user clicks on cart
      And user clicks on checkout
      And user enters first name John
      And user enters last name Doe
      And user enters zip code 123
      And user clicks Continue button
      Then I verify in Checkout overview page if the total amount for the added item is $8.63
      When user clicks Finish button
      Then Thank you header is shown in Checkout complete page
