import time

from browser import Driver, overlay

PAUSE_BETWEEN_SCENARIOS = 5
PAUSE_BETWEEN_STEPS = 1


@overlay
def before_feature(context, feature):
    if 'browser' in feature.tags:
        context.browser = Driver()


@overlay
def after_feature(context, feature):
    if 'browser' in feature.tags:
        context.browser.close()


@overlay
def before_scenario(context, scenario):
    pass


@overlay
def after_scenario(context, scenario):
    time.sleep(PAUSE_BETWEEN_SCENARIOS)


@overlay
def before_step(context, step):
    pass


@overlay
def after_step(context, step):
    time.sleep(PAUSE_BETWEEN_STEPS)
