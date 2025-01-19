Feature: Checkout an item from marketplace

    Scenario: User checkout an item
        #Given I logged in to the Blibli application
        When I search for a product 'iPhone 15'
        Then The product 'iPhone 15' will be displayed in the search results
        When I click on product 'iPhone 15'
        Then I will be redirected to product detail page for 'iPhone 15'
        When I click buy now button
        Then Product content details with variant and quantity selection will be be displayed
        When I select product 'color' variant with 'Yellow'
        And I select product 'capacity' variant with '128 GB'
        When I click buy now button
        Then The product checkout page will be displayed
        And Product with name 'iPhone 15' displayed on the checkout page
        And Product with quantity '1' displayed on the checkout page
        And Product with variant '128 GB, Yellow' displayed on the checkout page
        When I click pay button on the checkout page

