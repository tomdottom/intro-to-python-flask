@browser
Feature: Wilmington Web Devs links to Meetups

    Background: We know the url of the hompage
      Given the homepage url is "https://wilmingtonwebdev.github.io/"

    Scenario: User can see the next meetup is about Python
        Given we navigate to the homepage
         When we look at "Next Meetup"
         Then we see it is about "Python"
          and we see a link to the meetup page

    Scenario: User can see the last meetup is about Ruby
        Given we navigate to the homepage
         When we look at "Last Meetup"
         Then we see it is about "Ruby"
          and we see a link to the meetup page
