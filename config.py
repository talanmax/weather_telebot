from enum import Enum

token = "5690982401:AAErG4DmAkdnHBvJs2nkactdLhJL0opHpdA"

class States(Enum):
    S_START = "0"  #
    S_ENTER_NAME = "1"
    S_ENTER_CITY = "2"
    S_SEND_WEATHER_DAY = "3"
    S_SEND_MESSAGE_GOOD_BEY = "4"

