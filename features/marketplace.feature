Feature: Checkout an item from marketplace

    Scenario: User checkout an item
        #Given I logged in to the Blibli application
        When I search for a product 'iPhone 15'
        Then The product 'iPhone 15' will be displayed in the search results
        When I click on product 'iPhone 15'
        Then I will be redirected to product detail page for 'iPhone 15'
