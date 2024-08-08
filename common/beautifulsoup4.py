import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response


def create_parser(html, parser="html.parser"):
    soup = BeautifulSoup(html, parser)
    return soup


def get_element_by_id(soup: BeautifulSoup, id_attr: str):
    """指定した「id」属性の要素を1つ取得する"""
    return soup.find(id=id_attr)


def get_element_by_class(soup: BeautifulSoup, class_attr: str):
    """指定した「class」属性の要素を取得する(複数ある場合は最初の要素を取得)"""
    return soup.find(class_=class_attr)


def get_elements_by_classes(soup: BeautifulSoup, class_attr: str):
    """指定した「class」属性の要素を全て取得する"""
    return soup.find_all(class_=class_attr)
