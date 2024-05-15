#Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)

#class Bird():
#    def __init__(self, name):
#       self.name = name

#    def fly(self):
#        print('птица летает')
#class Ping(Bird):
#    pass

#p = Ping ("Сара")
#p.fly()
# Получается, что пингвины летают, а это неправильнго

#1. Создадим класс Bird и пропишем, что птица умеет летать:
class Bird():
    def fly(self):
        print("эта птица летает")

#2. Создадим класс Duck:
class Duck(Bird):
    def fly(self):
        print("Эта утка летает быстро")

def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)