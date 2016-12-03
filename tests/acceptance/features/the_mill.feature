@browser
Feature: TheMillSpace.com provides Xmas party information

    Background: We know the url of the hompage
      Given the homepage url is "http://themillspace.com/"

    Scenario: User can see Xmas party information
        Given we navigate to the homepage
         When we scroll to the Events section
         Then we see a link to the Holiday Party
          and we can follow in the Holiday Party page
