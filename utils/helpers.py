"""
Dane pomocnicze do testów na urządzeniach mobilnych z wykorzystaniem Appium - szczegóły w dokumentacji
"""

import os
import sys
from selenium.common.exceptions import InvalidSessionIdException
from datetime import datetime


ANDROID_BASE_CAPS = {
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': '7.1.1',
    'deviceName': 'Nexus 5',
    'browserName': 'chrome',
}

"""
IOS_BASE_CAPS = {
    'app': os.path.abspath('../apps/TestApp.app.zip'),
    'automationName': 'xcuitest',
    'platformName': 'iOS',
    'platformVersion': os.getenv('IOS_PLATFORM_VERSION') or '12.2',
    'deviceName': os.getenv('IOS_DEVICE_NAME') or 'iPhone 8 Simulator',
    # 'showIOSLog': False,
}
"""