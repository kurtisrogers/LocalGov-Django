Feature: LocalGov Django homepage
  As a citizen
  I want to visit the council homepage
  So that I can find services and information

  Scenario: Homepage displays council branding
    Given the sample content is loaded
    When I visit the homepage
    Then I should see "LocalGov Django"
    And I should see "Council services"

  Scenario: Homepage links to services
    Given the sample content is loaded
    When I visit the homepage
    Then I should see a link to "Waste and recycling"
