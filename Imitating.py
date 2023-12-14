class RockBand : #батьківський клас
    
    def __init__(self, vocalist, year, song): #конструктор , який визначає атрибути
        self.vocalist = vocalist
        self.year = year
        self.song = song

    def get_info(self): #функція виведення атрибутів
        print("Вокаліст:", self.vocalist , "Рік заснування:", self.year, "Відома пісня:", self.song)

class Nirvana (RockBand) : #створюємо класи , які наслідують батьківський
    pass

class ThreeDaysGrace (RockBand) :
    pass

class Skillet (RockBand) :
    pass

nirvana = Nirvana("Курт Кобейн", 1987 , "Smells like teen spirit") #створюємо об'єкт для класу Nirvana
nirvana.get_info()
threedaysgrace = ThreeDaysGrace("Адам Гонтьє", 1992 , "I hate ebverything about you") #створюємо об'єкт для класу ThreeDaysGrace
threedaysgrace.get_info()
skillet = Skillet("Джон Купер", 1996 , "Monster") #створюємо об'єкт для класу Skillet
skillet.get_info()