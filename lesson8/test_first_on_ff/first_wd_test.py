from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from webdrivermanager import GeckoDriverManager, ChromeDriverManager, IEDriverManager


def test_example():
    gdd = GeckoDriverManager()
    gdd.download_and_install()

    #
    option = FirefoxOptions()
    wd = webdriver.Firefox(options=option)
   # option = ChromeOptions
    #wd = webdriver.Chrome()
    wd.get("https://otus.ru/")
    assert wd.title == 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    wd.quit()



