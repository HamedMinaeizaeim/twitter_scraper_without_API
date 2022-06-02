from selenium import webdriver
# to add capabilities for chrome and firefox, import their Options with different aliases
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# import webdriver for downloading respective driver for the browser

from py_firefox_driver_manager import GeckoFireFoxdriverManager

class DriverInitilizer:
    def __init__(self, proxy=None):
        self.proxy = proxy

    def set_properties(self, browser_option):

        browser_option.add_argument(
            '--headless')  # runs browser in headless mode
        browser_option.add_argument('--no-sandbox')
        browser_option.add_argument("--disable-dev-shm-usage")
        browser_option.add_argument('--ignore-certificate-errors')
        browser_option.add_argument('--disable-gpu')
        browser_option.add_argument('--log-level=3')
        browser_option.add_argument('--disable-notifications')
        browser_option.add_argument('--disable-popup-blocking')
        return browser_option

    def setup_profile(self):
        """
        This code is setup the profile
        :param fileLocation: location of file to be save
        :return profile:
        """
        profile = webdriver.FirefoxProfile()
        #profile.set_preference("browser.download.dir", self.file_location);
        profile.set_preference("browser.download.folderList", 2);
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream");
        profile.set_preference("browser.download.manager.showWhenStarting", False);
        profile.set_preference("browser.helperApps.neverAsk.openFile",
                               "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream");
        profile.set_preference("browser.helperApps.alwaysAsk.force", False);
        profile.set_preference("browser.download.manager.useWindow", False);
        profile.set_preference("browser.download.manager.focusWhenStarting", False);
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
        profile.set_preference("browser.download.manager.showAlertOnComplete", False);
        profile.set_preference("browser.download.manager.closeWhenDone", True);
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference('permissions.default.stylesheet', 2)
        profile.set_preference('permissions.default.image', 2)
        profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        profile.set_preference("http.response.timeout", 500)
        profile.set_preference("dom.max_script_run_time", 500)
        return profile

    def set_driver_for_browser(self):
        """expects browser name and returns a driver instance"""
        browser_option = FirefoxOptions()
        if self.proxy is not None:
            options = {
                'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                'no_proxy': 'localhost, 127.0.0.1'
            }

            return webdriver.Firefox(executable_path=GeckoFireFoxdriverManager().install_geckodriver(),
                                     options=self.set_properties(browser_option), seleniumwire_options=options)


        return webdriver.Firefox(executable_path=GeckoFireFoxdriverManager().install_geckodriver(),
                                 options=self.set_properties(browser_option))


