# 4. Реализуйте класс Car (машина).
# Техническое задание:
#
# атрибуты: speed, color, name, 'is_police': (булево). speed - текущая скорость машины. Внимательно по отношению выбора атрибут класса/экземпляра.
# методы: go, stop, turn(direction), которые должны сообщать(выводить на экран), что машина поехала, остановилась, повернула (куда). turn(direction) - метод, принимающий параметр: направление поворота.
# Сами определите как вызов этих методов меняет скорость машины. На ваше усмотрение.
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# добавьте в базовый класс Car метод show_speed, который должен показывать текущую скорость автомобиля
# для классов TownCar и WorkCar переопределите метод 'show_speed'. При значении скорости машины свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Ограничения на скорость - очевидно данные. Где их нужно хранить?
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
class Car():
    def __init__(self, name, color, is_police, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Поехали ")

    def stop(self):
        print("Останавливаемся ")

    def turn(self, direction):
        print(f"Поворот на {direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")


class TownCar(Car):
    speed_limit = 60
    def __init__(self, name, color, speed):
        super().__init__(name, color, False, speed)
    def show_speed(self):
        print(f"Скорость: {self.speed}")
        if self.speed >= self.speed_limit:
            print("Превышение скорости")
        else:
            print("Скоростной лимит соблюдён")


class WorkCar(Car):
    speed_limit = 40
    def __init__(self, name, color, speed):
        super().__init__(name, color, False, speed)
    def show_speed(self):
        print(f"Скорость: {self.speed}")
        if self.speed >= self.speed_limit:
            print("Превышение скорости")
        else:
            print("Скоростной лимит соблюдён")

class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, False, speed)


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, True, speed)


tc = TownCar("Mazdа", "black", 120)
wc = TownCar("Susyki_Swift", "orange", 40)
sc = SportCar("Lamborghini_Murcielago", "yellow", 305)
pc = PoliceCar("FordFocus", "white", 234)

tc.show_speed()
wc.show_speed()
sc.show_speed()
pc.show_speed()

tc.go()
tc.stop()
tc.turn("Направо")
tc.turn("Налево")

print(pc.is_police)