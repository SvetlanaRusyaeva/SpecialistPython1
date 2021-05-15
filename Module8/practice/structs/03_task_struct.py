# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
lst = [1, -3, 0, 4,-8,15,-4,16,10]
kol = len(list(filter(lambda number: number <= 10, lst)))
print(kol)
positiv_sum = sum(list(filter(lambda number: number > 0, lst)))
print(positiv_sum)
lst2 = list(filter(lambda number: number%2==0, lst))
srednee = sum(lst2)/len(lst2)
print(srednee)
