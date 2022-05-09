# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# Условие задачи
# Техническое задание:
#
# duration - целое число: время в секундах. Вы можете вводить duration с клавиатуры или сразу занести в код.
# Формат вывода результата:
#
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры/Тесты:
#
# duration = 53: 53 сек
# duration = 153: 2 мин 33 сек
# duration = 4153: 1 час 9 мин 13 сек
# duration = 400153: 4 дн 15 час 9 мин 13 сек

duration = 400153

minutes = 60
hours = 3600
days = 86400

second = duration % (24 * hours)
day = duration // days
hour = second // hours
second %= hours
minute = second // minutes
second %= minutes

if duration > days:
    print(day, "дн", hour, "час", minute, "мин", second, "сек")
elif duration > hours:
    print(hour, "час", minute, "мин", second, "сек")
elif duration > minutes:
    print(minute, "мин", second, "сек")
else:
    print(second, "сек")