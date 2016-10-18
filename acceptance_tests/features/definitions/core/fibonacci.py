
import time
from aloe import step
from acceptance_tests.features.definitions.core.navigators._common import go_to_url
from acceptance_tests.features.definitions.core.page_interactors import fibonacci_page


@step('i open fibonacci page')
def user_go_to_page(step):
    time.sleep(1)
    go_to_url(step, '/fibonacci/')


@step(r'i see "([^"]*)" number')
def i_see_1_answer(step, text):
    fibonacci_page.check_answer(text)
    time.sleep(3)


