"""よく使う便利関数を定義する"""

import re
from typing import Any


def is_none_or_empty(check_value: Any) -> bool:
    """Noneと空文字の判定をする
    Noneまたは空文字: True、値判定あり: False
    """
    if check_value is None or check_value == "":
        return True
    return False


def address_to_address(value):
    """取得した生addressを加工してきれいにする。
    変更前：「所在地： 〒102-0091 東京都千代田区北の丸公園２－３」
    変更後：「東京都千代田区北の丸公園２－３」
    ※本処理は完璧でない。ファイルを確認し、修正されていないデータを手動で修正する
    """
    pattern = r"所在地：〒\d{3}-\d{4}"
    result = re.sub(pattern, "", value)

    return result


def get_prefecture_and_municipality_from_address(value):
    """
    所在地から都道府県と市区町村を抽出する
    ※本処理は完璧でない。ファイルを確認し、修正されていないデータを手動で修正する
    """
    pattern = """(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|
    富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村|宮古|富良野|別府|佐伯|黒部|小諸|塩尻|玉野|
    周南)市|(?:余市|高市|[^市]{2,3}?)郡(?:玉村|大町|.{1,5}?)[町村]|(?:.{1,4}市)?[^町]{1,4}?区|.{1,7}?[市町村])(.+)"""

    result = re.match(pattern, value)

    return result


def trim_breaks_tags(text: str):
    pattern = r"[\n\t\xa0]"
    result = re.sub(pattern, "", text)

    return result
