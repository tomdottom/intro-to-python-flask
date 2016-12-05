import time

from behave import given, when, then


@when(u'we scroll to the Events section')  # noqa
def step_impl(context):
    context.events_section = context.browser.find_element_by_id('events')
    context.browser.execute_script(
        "return arguments[0].scrollIntoView(true);", context.events_section)
    context.holiday_link_xpath = "//*[@class='events-item']//*[contains(text(), 'Holiday Party')]/parent::a"


@then(u'we see a link to the Holiday Party')  # noqa
def step_impl(context):
    context.holiday_link = context.browser.find_element_by_xpath(
        context.holiday_link_xpath)


@then(u'it takes us to the Holiday Party page')  # noqa
def step_impl(context):
    context.holiday_link.click()


@given(u'we navigate to Google')  # noqa
def step_impl(context):
    url = 'https://www.google.com'
    context.browser.get(url)
    assert url in context.browser.current_url


@when(u'we search for "{query}"')  # noqa
def step_impl(context, query):
    query_box = context.browser.find_element_by_xpath('//*[@id="lst-ib"]')
    query_box.send_keys(query, context.browser.KEYS.ENTER)
    context.holiday_link_xpath = "//a[@href='http://themillspace.com/events/mill-holiday-party/']"
    time.sleep(1)
