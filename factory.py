from selenium import webdriver


class WebDriverFactory:
    @staticmethod
    def get_web_driver(browser_name):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = True
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unknown browser {browser_name}")
