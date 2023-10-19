# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "24490919"))
    API_HASH = os.environ.get("API_HASH", "d1b3b15126c47dd4cb491553ee1db910")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6455342244:AAGVBztqflke4VMxs_2fVc14wFunR43Dllw")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1002092398392"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://spymusicbot:spymusicbot@cluster0.l4pi5sr.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5621114370"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/IDNCoderXRoot"
    TG_MAX_SIZE = 2040108421
