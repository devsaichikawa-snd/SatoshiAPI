from fastapi import FastAPI

from urls.snd_url import router
from src.data_import import import_snd_data, import_publicGym_data
from src.gym_webscraping import web_scraping
from src.gym_data_cleansing import data_cleansing


app = FastAPI()
app.include_router(router)


def __inport_snd_data_controller():
    """SNDの集計ファイルを取り込む"""
    import_snd_data()


def __inport_gym_controller():
    """公共体育館のデータ収集および集計ファイルの取り込み"""
    # gym_list = web_scraping()
    # if gym_list:
    #     data_cleansing(gym_list)
    # else:
    #     print("gym_listがありません。")
    import_publicGym_data()


if __name__ == "__main__":
    print("Hello SATOSHI!")
    # __inport_snd_data_controller()
    __inport_gym_controller()
