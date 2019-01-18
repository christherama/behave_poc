from behave import *

from api.models import User


@given("a user exists with email {email}")
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    :type email: str
    """
    User.objects.create(email=email)


@when("a API request is made to {url}")
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
