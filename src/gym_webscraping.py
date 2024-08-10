from common.beautifulsoup4 import (
    get_html,
    create_parser,
    get_elements_by_classes,
)
from config.logger import log_decorator
from common.const import SPOLAND_URL


@log_decorator
def web_scraping():
    """スポランドのサイトにアクセスしてジムの情報を取得する"""
    global_list = []

    for page in range(1, 59):
        # 1~58p全てでスクレイピングする
        aaaaa
        url = f"{SPOLAND_URL}{page}"
        response = get_html(url)
        if response.status_code == 200:

            soup = create_parser(response.text)

            # 施設名称取得
            elem_target_titles = []
            elems_title = get_elements_by_classes(soup, "fa_name")
            for elem_title in elems_title:
                elem_target_titles.append(elem_title.text)

            # 住所取得
            elems_address = get_elements_by_classes(soup, "fa_address")
            elem_target_addresses = [
                elem_address.text for elem_address in elems_address
            ]

            # リストの中から「アクセス」要素を削除する
            delete_elem = "アクセス"
            elem_target_addresses = [
                item
                for item in elem_target_addresses
                if delete_elem not in item
            ]

            # 要素の結合
            target_list = [
                list(items)
                for items in zip(elem_target_titles, elem_target_addresses)
            ]

            global_list.append(target_list)
        break

    return global_list
