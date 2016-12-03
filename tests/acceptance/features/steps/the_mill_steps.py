from behave import given, when, then


@when(u'we scroll to the Events section')  # noqa
def step_impl(context):
    context.events_section = context.browser.find_element_by_id('events')
    context.browser.execute_script(
        "return arguments[0].scrollIntoView(true);", context.events_section)


@then(u'we see a link to the Holiday Party')  # noqa
def step_impl(context):
    context.holiday_link = context.events_section.find_element_by_xpath(
        "//a/*[contains(text(), 'Holiday Party')]/parent::a")


@then(u'we can follow in the Holiday Party page')  # noqa
def step_impl(context):
    context.holiday_link.click()
