from common.beautifulsoup4 import (
    get_html,
    create_parser,
    get_elements_by_classes,
    get_element_by_a,
)
from config.logger import log_decorator
from common.const import SPOLAND_URL


@log_decorator
def web_scraping():
    """スポランドのサイトにアクセスしてジムの情報を取得する"""
    global_list = []

    # 1~58p全てでスクレイピングする
    for page in range(1, 59):
        url = f"{SPOLAND_URL}{page}"
        response = get_html(url)

        if response.status_code == 200:
            soup = create_parser(response.text)

            # 「施設名称」と「ホームメイトの施設別URL」を取得
            elem_titles = []
            elem_links = []
            elems_target_list = get_elements_by_classes(soup, "fa_name")
            for elem_title in elems_target_list:
                # 「施設名称」を格納する
                elem_titles.append(elem_title.text)

                # 「url」を格納する
                link = get_element_by_a(elem_title, get_link_flag=True)
                spoland_url = f"https://www.homemate-research-gym.com{link}"
                elem_links.append(spoland_url)

            # 住所の取得
            elems_address = get_elements_by_classes(soup, "fa_address")
            elem_target_addresses = [
                elem_address.text for elem_address in elems_address
            ]

            # 住所リストの中から「アクセス」要素を削除する
            delete_elem = "アクセス"
            elem_target_addresses_after = [
                item
                for item in elem_target_addresses
                if delete_elem not in item
            ]

            # 施設名、住所、URLを一つのListにまとめる
            target_list = [
                list(items)
                for items in zip(
                    elem_titles,
                    elem_target_addresses_after,
                    elem_links,
                )
            ]

            global_list.append(target_list)

        else:
            raise Exception("Responseが正常に返却されていません。")

    return global_list
