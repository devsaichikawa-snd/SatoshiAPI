import os
from pathlib import Path

from db.db_settings import get_db_engine, get_session, dispose_db_engine
from common.const import (
    SND_BT_LIST_FILE_NAME,
    PUBLIC_GYM_LIST_FILE_NAME,
    PUBLIC_GYM_LIST_SHEET_NAME,
)
from common.excel import (
    read_workbook,
    save_and_close_book,
    read_sheet,
    read_cell,
)
from common.util import is_none_or_empty
from models.snd_model import SndBroadcast
from models.public_gym_model import PublicGym


BASE_DIR = Path(__file__).resolve().parent.parent
SND_BT_LIST_FILE_PATH = os.path.join(BASE_DIR, SND_BT_LIST_FILE_NAME)
PUBLIC_GYM_LIST_FILE_PATH = os.path.join(BASE_DIR, PUBLIC_GYM_LIST_FILE_NAME)


def import_snd_data():
    """SndBroadcastテーブルにsnd_bt_listを取り込む処理"""

    wb = read_workbook(SND_BT_LIST_FILE_PATH)
    ws = read_sheet(wb)
    print("snd_bt_list.xlsxを開きました")

    # DB接続
    engine = get_db_engine()
    session = get_session()
    print("DBに接続しました。")

    # snd_bt_list.xlsxからデータを取得する
    row = 2
    while True:

        broadcast_year = read_cell(ws, row, 2, for_database=True)

        # 空行に当たったら、終了
        if is_none_or_empty(broadcast_year):
            break

        broadcast_month = read_cell(ws, row, 3, for_database=True)
        broadcast_date = read_cell(ws, row, 4, for_database=True)
        broadcast_content = read_cell(ws, row, 5, for_database=True)
        assistant_1 = read_cell(ws, row, 6, for_database=True)
        assistant_2 = read_cell(ws, row, 7, for_database=True)
        guests = read_cell(ws, row, 8, for_database=True)
        remarks = read_cell(ws, row, 9, for_database=True)

        model = SndBroadcast(
            broadcast_year=broadcast_year,
            broadcast_month=broadcast_month,
            broadcast_date=broadcast_date,
            broadcast_content=broadcast_content,
            assistant_1=assistant_1,
            assistant_2=assistant_2,
            guests=guests,
            remarks=remarks,
        )

        session.add(model)
        row += 1

    session.commit()
    print("DBにINSERTが完了しました。")

    # Excelを閉じる
    save_and_close_book(wb)
    # DBと切断
    session.close()
    # エンジンの破棄
    dispose_db_engine(engine)


def import_publicGym_data():
    """SndBroadcastテーブルにsnd_bt_listを取り込む処理"""

    wb = read_workbook(PUBLIC_GYM_LIST_FILE_PATH)
    ws = read_sheet(wb, PUBLIC_GYM_LIST_SHEET_NAME)
    print("public_gym_list.xlsxを開きました")

    # DB接続
    engine = get_db_engine()
    session = get_session()
    print("DBに接続しました。")

    # public_gym_list.xlsxからデータを取得する
    row = 2
    while True:

        facility_name = read_cell(ws, row, 2, for_database=True)

        # 空行に当たったら、終了
        if is_none_or_empty(facility_name):
            break

        prefecture = read_cell(ws, row, 3, for_database=True)
        municipality = read_cell(ws, row, 4, for_database=True)
        address = read_cell(ws, row, 5, for_database=True)
        telephone = read_cell(ws, row, 6, for_database=True)
        url = read_cell(ws, row, 7, for_database=True)
        training_room_flag = read_cell(ws, row, 8, for_database=True)

        model = PublicGym(
            facility_name=facility_name,
            prefecture=prefecture,
            municipality=municipality,
            address=address,
            telephone=telephone,
            url=url,
            training_room_flag=training_room_flag,
        )

        session.add(model)
        row += 1

    session.commit()
    print("DBにINSERTが完了しました。")

    # Excelを閉じる
    save_and_close_book(wb)
    # DBと切断
    session.close()
    # エンジンの破棄
    dispose_db_engine(engine)
