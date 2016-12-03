import time

from selenium import webdriver


def before_feature(context, feature):
    if 'browser' in feature.tags:
        context.driver = webdriver.Chrome()


def after_feature(context, feature):
    if 'browser' in feature.tags:
        context.driver.close()


def before_step(context, step):
    pass


def after_step(context, step):
    time.sleep(1)
