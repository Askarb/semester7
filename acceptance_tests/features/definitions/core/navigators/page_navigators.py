from acceptance_tests.features.definitions.core.navigators import _common


def go_to_client_page(step):
    url = '/client'
    _common.go_to_url(step, url)
