from behave import *
from behave.model import AutoMock

from api.models import User
from api.services import UserService, UserNotFoundException


@given("a user exists with a specified email address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.mocks = AutoMock(spec=User, target="api.services.User",
                             return_values={"objects.get": User(email='exists@email.com')})


@when("the UserService is called to retrieve that user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = UserService.find(email='exists@email.com')


@then("the service successfully retrieves that user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test.assertEquals(context.user.email, 'exists@email.com')


@given("a user with a specified email address does not exist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.mocks = AutoMock(spec=User, target="api.services.User", return_values={"DoesNotExist": User.DoesNotExist},
                             side_effects={"objects.get": User.DoesNotExist()})


@when("the UserService is called to retrieve the user with that email address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        UserService.find(email='doesnotexist@email.com')
        context.exception = None
    except Exception as e:
        context.exception = e


@then("the service raises a UserNotFoundException")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test.assertIsInstance(context.exception, UserNotFoundException)
