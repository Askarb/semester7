from aloe import before, world, after
from django.core.management import call_command
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from django.conf import settings
import os
import shutil


@before.all
def before_all():
    # call_command('syncdb',  interactive=False)
    # call_command('migrate', interactive=False)
    world.browser = webdriver.Firefox(getProfile())
    world.browser.get('')
    world.browser.set_window_size(1024, 768)
    world.browser.implicitly_wait(1)


@after.all
def after_all():
    world.browser.quit()


def getProfile():
    downloadPath = os.path.join(settings.BASE_DIR, 'features', 'resources', 'downloads')
    profile = FirefoxProfile()
    # profile.set_preference("browser.download.folderList", 2)
    # profile.set_preference("browser.download.manager.showWhenStarting", False)
    # profile.set_preference("browser.download.dir", downloadPath)
    # profile.set_preference("browser.helperApps.neverAsk.openFile",
    #                        "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
    # profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
    #                        "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
    # profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    # profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    # profile.set_preference("browser.download.manager.focusWhenStarting", False)
    # profile.set_preference("browser.download.manager.useWindow", False)
    # profile.set_preference("browser.download.manager.showAlertOnComplete", False)
    # profile.set_preference("browser.download.manager.closeWhenDone", False)
    return profile


@before.each_example
def before_each_example(scenario, outline, steps):
    pass
    # call_command('restore_db', interactive=False, verbosity=0)



