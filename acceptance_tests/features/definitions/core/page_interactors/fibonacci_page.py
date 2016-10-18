from aloe import world


def check_answer(text):
    world.browser.find_element_by_xpath('//p/i[text()="%s"]' % text)
