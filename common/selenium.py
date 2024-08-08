from typing import Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_web_driver(url: str, option: Any = None) -> webdriver.Chrome:
    """WebDriverを生成する"""
    if url is None or url == "":
        raise ValueError("urlが存在しません。")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get(url)
    print(f"{url}に接続しました。")

    return driver


def disconnect(driver: webdriver.Chrome) -> None:
    """WebDriverを切断する"""
    driver.close()
    print("WebDriverは切断されました。")


def get_element_by_id(driver: webdriver.Chrome, id_attr: str) -> Any:
    """指定した「id」属性の要素を1つ取得する"""
    return driver.find_element(By.ID, id_attr)


def get_element_by_class(driver: webdriver.Chrome, class_attr: str) -> Any:
    """指定した「class」属性の要素を1つ取得する"""
    return driver.find_element(By.CLASS_NAME, class_attr)


def get_elements_by_classes(driver: webdriver.Chrome, class_attr: str) -> Any:
    """指定した「class」属性の要素を全て取得する()"""
    return driver.find_elements(By.CLASS_NAME, class_attr)


def get_element_by_linktext(driver: webdriver.Chrome, class_attr: str) -> Any:
    """指定した「a」属性の要素を1つ取得する"""
    return driver.find_element(By.LINK_TEXT, class_attr)


def switch_browser_tabs(driver: webdriver.Chrome) -> None:
    """ブラウザのタブを右に1つ移動する"""
    driver.switch_to.window(driver.window_handles[1])


def push_button_in_javascript(driver: webdriver.Chrome, js_code: str) -> None:
    """javascriptが埋め込まれたボタンを押下する

    サンプル:<input type="button" value="Excel" onclick="javascript:excelout()">
    """
    driver.execute_script(js_code)


def push_link_anchor_text(driver: webdriver.Chrome, link_elem: Any) -> None:
    """aタグのリンク(ボタン)を押下する

    サンプル:<input type="button" value="Excel" onclick="javascript:excelout()">
    """
    driver.execute_script("arguments[0].click();", link_elem)
