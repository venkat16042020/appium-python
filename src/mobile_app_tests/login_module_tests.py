from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities1 = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app=r'C:\Users\venkat.kamani\PycharmProjects\MobileTestAutomatoin\APKs\app-release.apk',
    language='en',
    locale='US'
)
appium_server_url = 'http://127.0.0.1:4723/wd/hub'


def test_test1():
    options = UiAutomator2Options()
    options.load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)
    print(driver.page_source)
    driver.find_element(by=AppiumBy.ID, value='userNameTxtBox').send_keys("aaaaaa")
    driver.find_element(by=AppiumBy.ID, value='pwdTxtBox').send_keys("bbbbbb")
    el = driver.find_element(by=AppiumBy.ID, value='orderBtnOnSignInScrn')
    el.click()
    print("test execution is done")


def login():
    options = UiAutomator2Options()
    options.load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)
    print(driver.page_source)
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Place your Order"]')
    el.click()
