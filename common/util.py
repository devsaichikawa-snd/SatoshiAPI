"""よく使う便利関数を定義する"""

from datetime import date
import glob
import os
from pathlib import Path
import time
from typing import Any
import shutil


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


def get_last_month(today: date, pattern: str) -> str:
    """前月日付を取得する
    Args:
        today(date): date.today()
        pattern(str): "yyyymm"や"mm"などの年月日の形式
    """
    year = today.year
    month = today.month
    # 前月の計算
    if month == 1:
        # 1月の場合は前年の12月になる
        year -= 1
        month = 12
    else:
        month -= 1

    if pattern == "yyyymm":
        previous_date = f"{year}{month:02}"
    elif pattern == "mm":
        previous_date = f"{month:02}"
    elif pattern == "m月":
        previous_date = f"{month}月"
    else:
        raise ValueError("引数を確認してください。")

    return previous_date


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
