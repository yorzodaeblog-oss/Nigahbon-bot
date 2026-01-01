from json import load
from telebot.types import BotCommand
from pathlib import Path

#main settings
TOKEN = '7829726510:AAGd3vLFMksiTJFbOrhOmZvJrWTajNFtCpc' # orig
BOT_NAME = '@Nigahbonchat_bot'
LANG_FILE = 'lang.json'
with open(file=LANG_FILE, mode='r', encoding='utf-8') as file: LANGUAGE = load(file)
FORMAT_DATE = "%Y-%m-%d"
POLY_WIDTH = '8x8'
BOMBS = '1/5'
CBOMBS = [8,10,12,14]
CALL_DATA = [f"{ii}.{i}" for i in range(int(POLY_WIDTH.split('x')[0])) for ii in range(int(POLY_WIDTH.split('x')[1]))]
ADMIN_ID = 6724504799
KEY_PRICE = 50
PRO_PRICE = 100
TEXTURE_PRICE = 10
LENKEY = 20
COUNTKEY = 5

#command settings
MAIN_COMMANDS = ['start','play']
SETTING_BTNS = {
    "set_lang": {
        "ru" : "Сменить язык🔤",
        "tj" : "Ивази забон🔤"
    },
    "set_texture": {
        "ru" : "Изменить текстуры бомб💣",
        "tj" : "Ивази расми бомба💣"
    },
    "set_level": {
        "ru": "Уровень сложности📊",
        "tj": "Дараҷаи душворӣ📊"
    }
}
SHOP_BTNS = {
    "buy_key": "Ключи TrasherBot - 50 Бомбкоин",
    "buy_prem": "ПРО TrasherBot - 100 Бомбкоин"
}
LEVEL_BTNS = {
    "level_8": {"ru": "Легко", "tj": "Осон"},
    "level_10": {"ru": "Средне", "tj": "Миёна"},
    "level_12": {"ru": "Сложно", "tj": "Мушкил"},
    "level_14": {"ru": "Эксперт", "tj": "Олӣ"},
}
SET_COMMANDS = [
    BotCommand('start', "Запустить бота"),
    BotCommand('play', "Начать игру"),
    BotCommand('setting', "Настройки бота"),
    BotCommand('info', "Информация о себе"),
    BotCommand('buy', "Магазин")
]

#database settings
DB_NAME = 'bomber.db'
TABLE_USERS = 'users'
PARAMETERS_USER = "id INTEGER, " \
    "ln TEXT, " \
    "time TEXT, " \
    "cw INTEGER, " \
    "bal REAL, " \
    "texture TEXT, " \
    "record INTEGER, " \
    "level INTEGER," \
    "status TEXT"
STOLB_USER = "id, ln, time, cw, bal, texture, record, level, status"
TABLE_NAME_KEY = 'keys'
PARAMETER_KEY = "id INTEGER"
STOLB_KEY = "id, key, start_time, end_time, count"
db_trasherbot = Path('.').absolute().parent.joinpath('bot_trasher').joinpath('trash.db')

#map settings
MAPGAME = {"0": "⬜️", "1": "1⃣", "2": "2⃣", "3": "3⃣", "4": "4⃣", "5": "5⃣", "6": "6⃣", "7": "7⃣", "8": "8⃣", "b": "🧨"}

