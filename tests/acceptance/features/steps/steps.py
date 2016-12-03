from behave import given, when, then


@given(u'the homepage url is "{homepage_url}"')  # noqa
def step_impl(context, homepage_url):
    context.homepage_url = homepage_url


@given(u'we navigate to the homepage')  # noqa
def step_impl(context):
    context.browser.get(context.homepage_url)
    assert context.homepage_url in context.browser.current_url


@when(u'we look at "{meetup}"')  # noqa
def step_impl(context, meetup):
    try:
        context.next_meetup = context.browser.find_element_by_xpath(
            "//*[contains(text(), '{}')]/parent::*".format(meetup))
    except IndexError:
        raise Exception('Could not find next meetup')


@then(u'we see it is about "{subject}"')  # noqa
def step_impl(context, subject):
    meetup_title = context.next_meetup.find_element_by_xpath('*//h1').text
    assert subject in meetup_title


@then(u'we see a link to the meetup page')  # noqa
def step_impl(context):
    next_meetup = context.next_meetup.find_element_by_tag_name('a')
    next_meetup_link = next_meetup.get_attribute('href')
    next_meetup_title = next_meetup.text
    assert next_meetup_title == 'Sign up to the'
    assert next_meetup_link == 'https://www.meetup.com/Wilmington-DE-Web-Dev-Meetup/events/235845658/'
