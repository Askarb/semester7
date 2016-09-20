from acceptance_tests.features.definitions.core.navigators import _common


def go_to_login_page(step):
    url = '/'
    _common.go_to_url(step, url)


