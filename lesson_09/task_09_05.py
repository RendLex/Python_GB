# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Техническое задание:
#
# атрибут title (название)
# метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# Подумайте о том, имеет ли смысл при переопределении draw использовать draw базового класса.
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title}: ", end="")
        super().draw()

class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}: ", end="")
        super().draw()

class Handle(Stationery):
    def draw(self):
        print(f"{self.title}: ", end="")
        super().draw()

p1 = Pen("Шариковая Ручка")
p1.draw()
p2 = Pencil("Простой Карандаш")
p2.draw()
p3 = Handle("МАРКЕР")
p3.draw()