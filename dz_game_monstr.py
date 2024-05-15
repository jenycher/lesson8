from abc import ABC, abstractmethod

# создадим абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
# создадим классы оружия
class Sword(Weapon):
    def attack(self):
        return "Удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Выстрел из лука"


class Monster:
    pass

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def fight(self, monster):
        if self.weapon:
            print(f"{self.name} выбирает {self.weapon.__class__.__name__}.")
            print(f"{self.name} {self.weapon.attack()}.")
            print(f"{monster.__class__.__name__} побежден!")
        else:
            print("Боец не выбрал оружие!")
fighter = Fighter("Боец")
sword = Sword()
bow = Bow()

fighter.changeWeapon(sword)
monster = Monster()
fighter.fight(monster)

fighter.changeWeapon(bow)
fighter.fight(monster)