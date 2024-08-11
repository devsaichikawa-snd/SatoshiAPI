import os
from pathlib import Path

from common.excel import (
    read_workbook,
    save_and_close_book,
    read_sheet,
    write_cell,
)
from common.const import (
    PUBLIC_GYM_LIST_FILE_NAME,
    PUBLIC_GYM_LIST_SHEET_NAME,
)
from models.public_gym_model import PublicGymExcel
from common.util import (
    address_to_address,
    get_prefecture_and_municipality_from_address,
    trim_breaks_tags,
)


BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = os.path.join(BASE_DIR, PUBLIC_GYM_LIST_FILE_NAME)


def data_cleansing(gym_list: list):
    """データクレンジング処理"""
    wb = read_workbook(FILE_PATH)
    ws = read_sheet(wb, PUBLIC_GYM_LIST_SHEET_NAME)

    # スクレイピング結果→Model
    model_list = []
    for element in gym_list:
        # Page単位で分解する
        for sublist in element:
            # 施設単位で分解する
            public_gym_excel_model = PublicGymExcel()
            for k, value in enumerate(sublist):
                # 施設情報
                if k == 0:
                    public_gym_excel_model.facility_name = value
                elif k == 1:
                    trim_value = trim_breaks_tags(value)
                    address = address_to_address(trim_value)
                    result = get_prefecture_and_municipality_from_address(
                        address
                    )
                    if result:
                        public_gym_excel_model.prefecture = result.group(1)
                        public_gym_excel_model.municipality = result.group(2)
                    public_gym_excel_model.address = address
                elif k == 2:
                    public_gym_excel_model.url = value

            model_list.append(public_gym_excel_model)

    # public_gym_list.xlsxに書き込み
    row = 2
    for model in model_list:
        write_cell(ws, row, 2, model.facility_name)
        write_cell(ws, row, 3, model.prefecture)
        write_cell(ws, row, 4, model.municipality)
        write_cell(ws, row, 5, model.address)
        write_cell(ws, row, 7, model.url)

        row += 1

    # 保存して閉じる
    save_and_close_book(wb, FILE_PATH, True)
