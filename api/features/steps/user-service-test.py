from behave import *

from api.models import User
from api.services import UserService, UserNotFoundException


@given("a user exists with a specified email address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    User.objects.create(email='exists@email.com')


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
    pass


@when("the UserService is called to retrieve the user with that email address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.user = UserService.find(email='doesnotexist@email.com')
        context.exception = None
    except Exception, e:
        context.exception = e


@then("the service raises a UserNotFoundException")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test.assertIsInstance(context.exception, UserNotFoundException)
