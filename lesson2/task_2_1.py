# 1. Выяснить тип результата следующих выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
# Техническое задание:
# Вывести на экран тип выражения и отдельно проверить является ли полученный тип целым числом.

var = 31
multiplication = var * 3
division = var / 3
integer_division = var // 2
exponentiation = var ** 2

lst1 = [multiplication, division, integer_division, exponentiation]

for meaning in lst1:
    print(meaning, type(meaning))
    if isinstance(meaning, float):
        print("Целое число?", meaning.is_integer())
    else:
        print("Целое число? Folse")