from .settings import *


GHERKIN_TEST_CLASS = 'aloe_django.TestCase'
GHERKIN_TEST_RUNNER = 'aloe_django.runner.GherkinTestRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}

INSTALLED_APPS += (
    'django_jenkins',
    'aloe_django',
    'django_nose',
    'acceptance_tests',
)