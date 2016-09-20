from aloe import world
from acceptance_tests.features.definitions.core.common_actions import enter_text_info_text_field, user_clicks_button


def user_type_number(text, field_name):
    xpath = '//input[@name="%s"]' % field_name
    enter_text_info_text_field(xpath, text)


def user_click_submit_button():
    xpath = '//input[@type="submit"]'
    user_clicks_button(xpath)


def check_not_possible_text(text):
    world.browser.find_element_by_xpath('//span[@id="result"][text()="%s"]' % text)


def check_1_answer(text):
    world.browser.find_element_by_xpath('//span[@id="result"][text()="x: %s"]' % text)


def check_2_answer(text, text2):
    xpath = '//span[@id="result"]/i[1][text()="x1: %s"]' % text
    xpath2 = '//span[@id="result"]/i[2][text()="x2: %s"]' % text2
    world.browser.find_element_by_xpath(xpath)
    world.browser.find_element_by_xpath(xpath2)




