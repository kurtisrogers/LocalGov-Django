Feature: LocalGov Django services
  As a citizen
  I want to browse council services
  So that I can complete tasks online

  Scenario: Services list page
    Given the sample content is loaded
    When I visit the services page
    Then I should see "Council tax"

  Scenario: Service detail page
    Given the sample content is loaded
    When I visit "/services/waste-recycling/"
    Then I should see "Waste and recycling"
