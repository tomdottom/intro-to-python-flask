from behave import given, when, then
from jsonschema import validate
from jsonpath_rw import parse
import requests

from excs import BddFailure
import schemas

USAGE = '''\n
Usage:

    behave -D "server={{ hostname }}"
'''


@given(u'I have a server to test')  # noqa
def step_impl(context):
    context.server = context.config.userdata.get('server')
    if context.server is None:
        raise BddFailure(msg=USAGE)


@when(u'I call the "{endpoint}" endpoint')  # noqa
def step_impl(context, endpoint):
    url = '{server}{endpoint}'.format(server=context.server, endpoint=endpoint)
    context.response = requests.get(url)


@then(u'I receive a "{status_code}" response')  # noqa
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code), (
        "Expected to receive a 200 repsonse, instead got a {}".format(
            context.response.status_code))


@then(u'the response conforms to the "{schema}" schema')  # noqa
def step_impl(context, schema):
    validate(context.response.json(), getattr(schemas, schema))


@then(u'the response "{jsonpath}" datum is "{expected}"')
def step_impl(context, jsonpath, expected):
    jsonpath_expr = parse(jsonpath)
    values = [match.value for match in jsonpath_expr.find(context.response.json())]
    assert values == [expected], (
        'Expected {} got {}'.format(expected, values))
