# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here

m = int(input())

if m==12 or m>=1 and m<3:
    print("winter")
elif m>=3 and m<=5:
    print("spring")
elif m>=6 and m<=8:
    print("summer")
else:
    print("autumn")
