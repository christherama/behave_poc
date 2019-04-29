from api.models import User
from api.services import UserNotFoundException, UserService
from behave import *
from behave.model import AutoMock


@given("a user exists with email {email}")
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    :type email: str
    """
    context.mocks = [
        AutoMock(spec=UserService, target="api.views.UserService", find__return_value=User(email=email))
    ]


@when("an API request is made to GET {url}")
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    context.response = context.test.client.get(url)


@then("the response status is {status:d}")
def step_impl(context, status):
    """
    :type context: behave.runner.Context
    :type status: int
    """
    context.test.assertEquals(context.response.status_code, status)


@given("a user does not exist with email `doesnotexist@email.com`")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.mocks = [
        AutoMock(spec=UserService, target="api.views.UserService", find__side_effect=UserNotFoundException())
    ]


@then("the response status is `404`")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test.assertEquals(context.response.status_code, 404)


@then("the UserService is called to retrieve that user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.mocks.get(UserService).find.assert_called_once()
