@browser
Feature: TheMillSpace.com provides Xmas party information

    Background: We know the url of the hompage
      Given the homepage url is "http://themillspace.com/"

    Scenario: User can see Xmas party information on TheMillSpace Website
        Given we navigate to the homepage
         When we scroll to the Events section
         Then we see a link to the Holiday Party
          and it takes us to the Holiday Party page

    Scenario: User can find Xmas party information from Google
        Given we navigate to Google
         When we search for "the mill space wilmington de holiday party"
         Then we see a link to the Holiday Party
          and it takes us to the Holiday Party page
