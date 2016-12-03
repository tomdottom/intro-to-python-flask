@browser
Feature: Homepage contains essential elements

    Scenario Outline: User can see the <element>
        Given we navigate to the homepage
         When we look for a "<element>"
         Then it is present on the page

    Examples: Essential Elements
        | element       |
        | menu          |
        | title         |
        | main content  |
