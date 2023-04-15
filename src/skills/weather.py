import requests
from num2words import num2words
from api_tokens import OPEN_WEATHER_TOKEN

class Weather():
    def __init__(self, city='Novosibirsk', lang='ru', units='metric'):
        self.__city = city
        self.__lang = lang
        self.__units = units
        self.__appid = OPEN_WEATHER_TOKEN

    def current_weather(self):
        params = {
            'q' : self.__city,
            'appid' : self.__appid,
            'lang' : self.__lang,
            'units' : self.__units
        }

        try:
            r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
            if r.status_code != 200:
                return False
        except Exception:
            return False

        return r.json()

    def beautify_weather(self, data):
        if not data:
            return False

        degree = round(data['main']['temp'])
        city = 'Чмомске' if self.__city == 'Omsk' else 'Сл+эйвсити'
        hot_or_cold = self.__hot_or_cold(degree)

        text = 'В ' + city + ' сейч+ас ' + hot_or_cold + '. '
        text += data['weather'][0]['description'] + '. '
        text += 'Скорость в+етра: ' + num2words(data['wind']['speed'], lang='ru') + ' метров в секунду.'
        return text

    def __hot_or_cold(self, degree):
        degree_text = num2words(degree, lang='ru')
        if degree > 0:
            return 'плюс ' + degree_text
        elif degree == 0:
            return degree_text + ' градусов'
        return degree_text
