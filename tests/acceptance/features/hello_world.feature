Feature: We can call the hello world api
  In order to check their sanity
  As as developer
  I want to check that I can call the "/api/v1/hello_world" endpoint

  Scenario: Call "/api/v1/hello_world" endpoint
    Given I have a server to test
     When I call the "/api/v1/hello_world" endpoint
     Then I receive a "200" response
      and the response conforms to the "HELLO_WORLD" schema
      and the response "hello" datum is "world"
