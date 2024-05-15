#Принцип инверсии зависимости (DIP, Dependency Inversion Principle)

#class Book():
#Создадим функцию чтения:
 #   def read(self):
#        print("Чтение интересной истории")

#Создадим класс StoryReader:
# class StoryReader():
#Создадим объект класса Book, чтобы связать оба класса между собой:
#     def __init__(self):
#         self.book = Book()
#     def tell_story(self):
#        self.book.read()
#Сейчас класс StoryReader напрямую очень сильно зависит от класса Book. Так быть не должно, части не должны зависеть друг от друга; они должны зависеть
# от абстракции (абстрактного класса).

from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

#Создадим класс, указав источником историй Book:
class Book(StorySource):
#Пропишем функцию get_story, на этот раз заполнив её:
    def get_story(self):
        print("Чтение интересной истории")

#Мы создали программу для класса Book. Теперь создадим аудиокнигу,
# Создадим класс AudioBook:
class AudioBook(StorySource):
#Создадим для этого класса функцию:
    def get_story(self):
        print("Чтение интересной истории вслух")

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = Book()
audioBook = AudioBook()

readerBook = StoryReader(book)
readerAudioBook = StoryReader(audioBook)

readerBook.tell_story()
readerAudioBook.tell_story()

