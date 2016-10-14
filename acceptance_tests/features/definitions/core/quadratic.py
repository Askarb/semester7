import time
from aloe import step
# from acceptance_tests.features.definitions.core.navigators.admin_navigator import go_to_login_page
from acceptance_tests.features.definitions.core.navigators._common import go_to_url
from acceptance_tests.features.definitions.core.page_interactors import quadratic_page



@step('i open "([^"]*)" page')
def user_go_to_page(step, page):
    go_to_url(step, '/%s/' % page)


@step('i enter into "([^"]*)" field a "([^"]*)"')
def i_enter_into_text_field(step, field_name, text):
    quadratic_page.user_type_number(text, field_name)
    time.sleep(1)


@step('click button submit')
def i_click_button_submit(step):
    quadratic_page.user_click_submit_button()


@step(r'i see "([^"]*)" text')
def i_see_not_possible_text(step, text):
    quadratic_page.check_not_possible_text(text)
    time.sleep(5)


@step(r'i see 1 answer "([^"]*)" text')
def i_see_1_answer(step, text):
    quadratic_page.check_1_answer(text)
    time.sleep(5)


@step(r'i see 2 answer "([^"]*)" and "([^"]*)" text')
def i_see_1_answer(step, text, text2):
    quadratic_page.check_2_answer(text, text2)
    time.sleep(5)


@step(r'i see "([^"]*)" error message in "([^"]*)" field')
def i_see_1_answer(step, text, field):
    quadratic_page.check_error_message(field, text)
    time.sleep(5)



