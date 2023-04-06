from enum import Enum

token = "6091645064:AAFzQGkcf3wMpZpir3EApkXEnEIGRc22npg"

class States(Enum):
    S_START = "0"  #
    S_ENTER_NAME = "1"
    S_ENTER_CITY = "2"
    S_SEND_WEATHER_DAY = "3"
