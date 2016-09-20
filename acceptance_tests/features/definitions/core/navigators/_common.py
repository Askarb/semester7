from aloe import step
from aloe import world
from aloe_django import django_url


def go_to_url(step, url):
    world.browser.get(django_url(step) + url)


