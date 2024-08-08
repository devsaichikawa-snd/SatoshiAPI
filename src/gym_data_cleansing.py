import traceback

from common.excel import (
    read_workbook,
    save_and_close_book,
    read_sheet,
    read_cell,
    write_cell,
)
from common.const import (
    WINDOWS_DOWNLOAS_DIR,
    PUBLIC_GYM_LIST_FILE_NAME,
    PUBLIC_GYM_LIST_SHEET_NAME,
)
from models.public_gym_model import PublicGymExcel
from common.util import address_to_address


def data_cleansing(gym_list: list):
    """データクレンジング処理"""
    wb = read_workbook(PUBLIC_GYM_LIST_FILE_NAME)
    ws = read_sheet(wb, PUBLIC_GYM_LIST_SHEET_NAME)

    # スクレイピング結果→Model
    model_list = []
    for i, element in enumerate(gym_list):
        for j, sublist in enumerate(element):
            public_gym_excel_model = PublicGymExcel()
            for k, value in enumerate(sublist):
                if k == 0:
                    public_gym_excel_model.facility_name = value
                if k == 1:
                    public_gym_excel_model.address = address_to_address(value)
            else:
                model_list.append(public_gym_excel_model)

    # 住所編集
    for i, model in enumerate(model_list):
        public_gym_excel_model.index = i

    row = 2
    for i, model in enumerate(model_list):
        row += i
        write_cell(ws, row, 1, i + 1)
        write_cell(ws, row, 2, model.facility_name)
        write_cell(ws, row, 4, model.address)

    # 保存して閉じる
    save_and_close_book(wb, f"../{PUBLIC_GYM_LIST_FILE_NAME}", True)


def data_cleansing_address(self):
    # ここからはExcelファイルを再開封し直接編集する
    excel_operation = ExcelOperation()
    wb, ws = excel_operation.read_excel(
        Const.PUBLIC_GYM_LIST_FILE, Const.PUBLIC_GYM_LIST_SHEET_NAME
    )

    try:
        model_list = []
        for row in range(2, ws.max_row + 1):
            model = GymExcelModel()
            model.facility_name = excel_operation.get_cell_value(ws, row, 1)
            model_list.append(model)

        print("箱完成")

        failure_list = []
        for i, model in enumerate(model_list):
            model.index = i
            i += 2
            model.address = excel_operation.get_cell_value(ws, i, 4)
            prefecture_and_municipality = (
                self.get_prefecture_and_municipality_from_address(
                    model.address
                )
            )
            if prefecture_and_municipality:
                model.prefecture = prefecture_and_municipality.group(1)
                model.municipality = prefecture_and_municipality.group(2)
            else:
                failure_list.append(model)
                model.index = Const.INT_UNSET

        print(len(failure_list))

        print("Excelから値を取得し、モデルに格納した。")

        for model in model_list:
            if model.index == -1:
                continue
            row = model.index + 2
            excel_operation.set_cell_value(ws, row, 2, model.prefecture)
            excel_operation.set_cell_value(ws, row, 3, model.municipality)
    finally:
        excel_operation.save_and_close_excel(
            wb, file=Const.PUBLIC_GYM_LIST_FILE, save_flag=True
        )
        del excel_operation  # デストラクタの起動
        print("処理が終了しました。")
