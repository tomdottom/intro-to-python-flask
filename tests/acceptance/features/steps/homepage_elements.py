from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException

from excs import BddFailure


@given(u'we navigate to the homepage')  # noqa
def step_impl(context):
    context.driver.get('http://localhost:5000')


NAME_ID_MAP = {
    "menu": "menu",
    "title": "title",
    "main content": "content",
}


@when(u'we look for a "{element}"')  # noqa
def step_impl(context, element):
    context.element = element
    context.element_id = NAME_ID_MAP[element]


@then(u'it is present on the page')  # noqa
def step_impl(context):
    try:
        context.elem = context.driver.find_element_by_id(context.element_id)
    except NoSuchElementException:
        raise BddFailure(msg='''
            Tried to find element {element} using id {id}
        '''.format(element=context.element, id=context.element_id))
