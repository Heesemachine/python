"""Об’єкт “Аудыо файл”
поля:
формат файлу;+
дата створення;+
тривалість;+
частота дискретизації;+
глибина кодування;+
методи
визначення «віку» файлу;+
визначення кількості точок збереження за вказаний проміжок часу;
визначення об’єму файлу з вказаною тривалістю.

"""
from datetime import date, datetime
def get_today_date():
    return date(datetime.today().year, datetime.today().month, datetime.today().day)
class audiofile():
    def __init__(self,formatfily, data_st, truvalist, chas_d, glybina_cod):
        self.formatfily = formatfily
        self.data_st = data_st
        self.truvalist = truvalist
        self.chas_d = chas_d
        self.glybina_cod = glybina_cod
    def age(self):
        return get_today_date().year - self.data_st.year

    def dots_for_save(self):
        return self.truvalist * self.chas_d # в секундах

    def vaga_fily(self):
        return self.chas_d * self.glybina_cod * self.truvalist # в Байтах.....

data_st = date(2021, 5, 1)
AudioFile = audiofile(input('Формат Файлу: '), input('Дата створення: '), int(input('Тривалість запису: ')),
int((input('Частота Дискритизації: ')), int(input('Глубина кодування: ')))
print(" Формат файлу: {0}\n Дата створення: {1}\n Тривалість запису: {2}\n Частота Дискритизації: {3:.2f}\n Глубина Кодування {4}\n"
      .format(AudioFile.formatfily, AudioFile.data_st, AudioFile.truvalist, AudioFile.chas_d, AudioFile.glybina_cod))


