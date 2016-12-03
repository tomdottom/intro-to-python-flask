from enum import Enum
import os

from jinja2 import Template
import selenium.webdriver

__file__dir__ = os.path.dirname(os.path.abspath(__file__))
with open(__file__dir__ + '/bdd-overlay.css') as fh:
    overlay_css = fh.read().replace('\n', ' ')
with open(__file__dir__ + '/bdd-overlay.html.j2') as fh:
    overlay_html_template = Template(fh.read())

OVERLAY = []

OVERLAY_TEMPLATE = """
    if (!document.getElementById('bdd-overlay-styles')) {
        var overlayStyles = document.createElement('style');
        overlayStyles.id = 'bdd-overlay-styles';
        document.head.appendChild(overlayStyles);
        overlayStyles.innerHTML = '%s';
    }

    var overlay = document.getElementById('bdd-overlay')
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'bdd-overlay';
        document.body.appendChild(overlay);
    }
    overlay.innerHTML = '%s';
"""


class BDDMessageType(Enum):
    Feature = 'Feature'
    Scenario = 'Scenario'
    Given = 'Given'
    When = 'When'
    Then = 'Then'
    And = 'And'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.value


class BDDMessageStatus(Enum):
    InProgress = 'bdd-in-progress'
    OK = 'bdd-ok'
    Failed = 'bdd-failed'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.value


class BDDMessage(object):

    DEFAULTS = {
        'Feature': BDDMessageStatus.OK,
        'Scenario': BDDMessageStatus.OK,
        'Given': BDDMessageStatus.InProgress,
        'When': BDDMessageStatus.InProgress,
        'Then': BDDMessageStatus.InProgress,
        'And': BDDMessageStatus.InProgress,
        BDDMessageType.Feature: (0, ': '),
        BDDMessageType.Scenario: (2, ': '),
        BDDMessageType.Given: (4, ' '),
        BDDMessageType.When: (5, ' '),
        BDDMessageType.Then: (5, ' '),
        BDDMessageType.And: (6, ' '),
    }

    def __init__(self, msg_type, description):
        self.type = BDDMessageType(msg_type)
        self.description = description
        self.status = self.DEFAULTS[msg_type]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '{}{}{}{}'.format(
            self.DEFAULTS[self.type][0] * '&nbsp;',
            self.type,
            self.DEFAULTS[self.type][1],
            self.description
        )

    def __eq__(self, other):
        return str(self) == str(other)


class Driver(selenium.webdriver.Chrome):

    BDD_MESSAGES_CACHE = None

    def __init__(self, *args, **kwargs):
        super(Driver, self).__init__(*args, **kwargs)

    def update_overlay(self, overlay_messages):
        self.BDD_MESSAGES_CACHE = overlay_messages
        self._update_overlay()

    def _update_overlay(self):
        msg = overlay_html_template.render(
            msgs=self.BDD_MESSAGES_CACHE
        ).replace('\n', ' ')
        overlay_script = OVERLAY_TEMPLATE % (overlay_css, msg)
        self.execute_script(overlay_script)

    def get(self, *args, **kwargs):
        super(Driver, self).get(*args, **kwargs)
        self._update_overlay()


def _add_to_bdd_overlay_messages(context, item):
    msg = BDDMessage(item.keyword, item.name)
    if msg.type == BDDMessageType.Feature:
        msg.status = BDDMessageStatus.OK
        if context._bdd_overlay_data['Feature'] != [msg]:
            context._bdd_overlay_data['Feature'] = [msg]
            context._bdd_overlay_data['Steps'] = []
            context._bdd_overlay_data['Scenario'] = []
        else:
            if item.status == 'failed':
                msg.status = BDDMessageStatus.Failed
            context._bdd_overlay_data['Feature'] = [msg]
    elif msg.type == BDDMessageType.Scenario:
        msg.status = BDDMessageStatus.OK
        if context._bdd_overlay_data['Scenario'] != [msg]:
            context._bdd_overlay_data['Scenario'] = [msg]
            context._bdd_overlay_data['Steps'] = []
        else:
            if item.status == 'failed':
                msg.status = BDDMessageStatus.Failed
            context._bdd_overlay_data['Scenario'] = [msg]
    else:
        if context._bdd_overlay_data['Steps'][-1:] != [msg]:
            context._bdd_overlay_data['Steps'].append(msg)
        else:
            if item.status == 'failed':
                msg.status = BDDMessageStatus.Failed
            else:
                msg.status = BDDMessageStatus.OK
            context._bdd_overlay_data['Steps'].pop()
            context._bdd_overlay_data['Steps'].append(msg)

    context._bdd_overlay_messages = (context._bdd_overlay_data['Feature'] +
                                     context._bdd_overlay_data['Scenario'] +
                                     context._bdd_overlay_data['Steps'])


def overlay(func):
    def wraps(*args, **kwargs):
        context, item = args
        try:
            context._bdd_overlay_messages
        except KeyError:
            context._bdd_overlay_messages = []
            context._bdd_overlay_data = {
                'Feature': [],
                'Scenario': [],
                'Steps': []
            }

        _add_to_bdd_overlay_messages(context, item)

        try:
            context.browser.update_overlay(context._bdd_overlay_messages)
        except AttributeError:
            pass

        return func(*args, **kwargs)
    return wraps
