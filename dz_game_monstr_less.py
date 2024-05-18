# Разбор домашнего задания
from abc import ABC, abstractmethod

#Создаём абстрактный класс, указываем декоратор:
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

#Создаём класс меча:
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

#Создаём класс лука:
class Bow(Weapon):
      def attack(self):
        print("Боец делает выстрел из лука")

#Создаём класс для бойца. Прописываем возможность менять оружие бойца. Прописываем возможность персонажа использовать оружие:
class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())

#Создаём класс монстра.
class Monster():
    pass

#Создаём объекты классов оружия:
sword1 = Sword()
bow1 = Bow()

#Создаём объект класса бойца:
fighter = Fighter(sword1)

#Наносим удар:
fighter.fight()

#Заменяем оружие:
fighter.changeWeapon(bow1)

#Стреляем из лука:
fighter.fight()