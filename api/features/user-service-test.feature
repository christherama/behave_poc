Feature: User service abstracts interactions with persistence layer

  @wip
  Scenario: Attempt to retrieve existing user is successful
    Given a user exists with a specified email address
     When the UserService is called to retrieve that user
     Then the service successfully retrieves that user


  Scenario: Attempt to retrieve non-existent user raises exception
    Given a user with a specified email address does not exist
     When the UserService is called to retrieve the user with that email address
     Then the service raises a UserNotFoundException
