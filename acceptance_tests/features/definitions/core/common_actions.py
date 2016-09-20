from aloe import world
from selenium.common.exceptions import WebDriverException


def enter_text_info_text_field(element_selector, text):
    field = world.browser.find_element_by_xpath(element_selector)
    field.clear()
    field.send_keys(text)


def user_clicks_button(xpath):
    link = world.browser.find_element_by_xpath(xpath)
    try:
        link.click()
    except WebDriverException:
        world.browser.execute_script("window.scrollBy(0, -150);")
        link.click()

