import pyautogui
from emunium.browsers import EmuniumSelenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
emunium = EmuniumSelenium(driver)


def test_scroll_and_move_to():
    driver.get("https://pypi.org/project/emunium/")

    footer = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/main/div[4]/div/div/div[1]/div[3]/h6[1]",
            )
        )
    )

    languages_element = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/main/div[4]/div/div/div[1]/div[3]/div[3]/ul/li[3]/strong",
            )
        )
    )

    print("scroll to the footer")
    time.sleep(1)

    print("move to the languages_element")
    emunium.scroll_to(footer)
    time.sleep(1)
    emunium.scroll_to(languages_element)

    time.sleep(1)

    footer_element = wait.until(
        EC.element_to_be_clickable(
            (
                By.CLASS_NAME,
                "footer",
            )
        )
    )

    print("scroll to the footer")
    time.sleep(1)
    emunium.scroll_to(footer_element)

    time.sleep(1)
    emunium.scroll_to(languages_element)
    time.sleep(1)
    driver.quit()


def test_scroll_and_move_to2():
    driver.get("https://pypi.org/project/emunium/")

    language = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/main/div[4]/div/div/div[1]/div[3]/h6[1]",
            )
        )
    )

    time.sleep(1)

    footer_element = wait.until(
        EC.element_to_be_clickable(
            (
                By.CLASS_NAME,
                "footer",
            )
        )
    )

    # pyautogui.scroll(-40)
    time.sleep(1)

    print("\n scroll to language")
    emunium.scroll_to(language)
    time.sleep(2)

    print("\n scroll to footer")
    emunium.scroll_to(footer_element)
    time.sleep(2)

    print("\n scroll to language")
    emunium.scroll_to(language)
    time.sleep(2)
    time.sleep(2)
    time.sleep(2)

    driver.quit()


test_scroll_and_move_to2()
