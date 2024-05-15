#Принцип разделения интерфейсов (ISP, Interface Segregation Principle)

#Создадим класс "Умный дом", внутрь которого мы встроим большое количество функций:
class SmartHouse():
#Создадим для этого дома функцию включения освещения:
    def turn_on_light(self):
        pass
    #Создадим функцию разогрева еды:
    def heat_food(self):
        pass
    #Создадим функцию для включения музыки:
    def turn_on_music(self):
         pass

#1. Создадим отдельный класс для включения/выключения света:
class Light():
    def turn_on_light(self):
        print("Свет включен")

#2. Создадим отдельный класс для разгорева еды:
class Food():
    def heat_food(self):
        print("Еда начала разогреваться")

#3. Создадим отдельный класс для управления музыкой:
class Music():
    def turn_on_music(self):
        print("Вкючаю подборку ваших любимых песен")

