
Feature: Endpoint for checking whether or not a user exists
  As an API consumer
  I want to make a request to check whether or not a user exists
  So that I know whether or not to create a new user

  Scenario Outline: User with identical email exists
    Given a user exists with email <email>
     When a API request is made to <url>
     Then the response status is <status>

    Examples:
    | email | url | status |
    | exists@email.com | /api/users/exists?email=exists@email.com | 200 |
    | exists@email.com | /api/users/exists?email=EXISTS@email.com | 200 |

  Scenario Outline: User does not exist
    Given a user exists with email <email>
     When a API request is made to <url>
     Then the response status is <status>

    Examples:
    | email | url | status |
    | exists@email.com | /api/users/exists?email=doesnotexist@email.com | 404 |