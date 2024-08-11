"""よく使う便利関数を定義する"""

from datetime import date
import glob
import os
from pathlib import Path
import re
import shutil
import time
from typing import Any


def get_project_dir() -> Path:
    """プロジェクトDirを生成する"""
    return Path.cwd()


def is_none_or_empty(check_value: Any) -> bool:
    """Noneと空文字の判定をする
    Noneまたは空文字: True、値判定あり: False
    """
    if check_value is None or check_value == "":
        return True
    return False


def get_today() -> date:
    """本日日付を取得する"""
    return date.today()


def from_str_to_date(value: str) -> date:
    """日付の型変換(str → date)"""
    datetyep_value = date.fromisoformat(value)
    return datetyep_value


def time_keeper(seconds: int):
    """待機時間を発生させる"""
    time.sleep(seconds)


def remove_day_str(value) -> str:
    """「日」の文字を削除する"""
    if value is not None:
        result = value.replace("日", "")
        return result
    return value


def remove_value(value, start, end):
    """指定した範囲の文字列を削除する

    Parameters:
        value: 対象の値
        start: 開始位置
        end: 終了位置
    """
    end_plus_one = end + 1
    return value[:start] + value[end_plus_one:]


def file_copy(original_file: str, copy_to: str):
    """File Copy"""
    shutil.copy2(original_file, copy_to)


def delete_file(files_path: str | list):
    """ファイルを削除する
    files_pathがlistで来たら、全部削除する
    """
    if isinstance(files_path, list):
        # 引数がリストの場合、全ファイルを削除
        for file in files_path:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")
    else:
        # 引数が単一のファイルパスの場合、そのファイルを削除
        try:
            os.remove(files_path)
            print(f"Deleted: {files_path}")
        except Exception as e:
            print(f"Error deleting {files_path}: {e}")


def get_files(dir_path: str, pattern: str = "*") -> list[str]:
    """指定したディレクトリ内のパターンに一致するファイルを全て取得する"""
    path = os.path.join(dir_path, pattern)
    files = glob.glob(path)
    return files


def create_timer():
    """処理時間計測の為に、時間を生成する"""
    return time.time()


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
