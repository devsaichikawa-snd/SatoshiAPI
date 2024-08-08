from fastapi import FastAPI

from urls.snd_url import router
from src.gym_webscraping import web_scraping
from src.gym_data_cleansing import data_cleansing


app = FastAPI()
app.include_router(router)


def __inport_data_controller():
    """SNDの集計ファイルを取り込む"""
    from src.snd_data_inport import import_data

    import_data()


def __inport_sym_controller():
    """公共体育館のデータ収集および集計ファイルの取り込み"""
    gym_list = web_scraping()
    if gym_list:
        print(gym_list)
    # data_cleansing(gym_list)


if __name__ == "__main__":
    print("Hello SATOSHI!")
    # __inport_data_controller()
    __inport_sym_controller()
