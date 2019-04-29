
Feature: Endpoint for checking whether or not a user exists
  As an API consumer
  I want to make a request to check whether or not a user exists
  So that I know whether or not to create a new user

  Scenario Outline: User with identical email exists
    Given a user exists with email <email>
     When an API request is made to GET <url>
     Then the response status is <status>

    Examples:
    | email | url | status |
    | exists@email.com | /api/users/exists?email=exists@email.com | 200 |
    | exists@email.com | /api/users/exists?email=EXISTS@email.com | 200 |

  @wip
  Scenario: User does not exist
    Given a user does not exist with email `doesnotexist@email.com`
     When an API request is made to GET /api/users/exists?email=doesnotexist@email.com
     Then the response status is 404
      And the UserService is called to retrieve that user