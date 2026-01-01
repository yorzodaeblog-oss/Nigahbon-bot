from dbhelper import DB
from setting import (TABLE_USERS, PARAMETERS_USER, FORMAT_DATE, STOLB_USER)
from datetime import datetime

db_bot = DB(TABLE_USERS,PARAMETERS_USER)
time = datetime.now()
db_date = time.strftime(FORMAT_DATE)

# db_bot.write((1653169072,'ru',db_date,22,6,"💣",0,8,'info'),STOLB_USER)
db_bot.update('status','start',1653169072)