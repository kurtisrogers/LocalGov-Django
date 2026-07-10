Feature: LocalGov Django search
  As a citizen
  I want to search the council website
  So that I can find relevant information

  Scenario: Sitewide search returns results
    Given the sample content is loaded
    When I search for "council tax"
    Then I should see "Pay your council tax"
