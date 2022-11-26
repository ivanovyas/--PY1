money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = spend - salary  # На сколько уходим в минус каждый месяц
while delta < money_capital:  # Пока подушка безопасности покрывает расходы сверх зарплаты
    delta = spend - salary
    month += 1
    money_capital -= delta
    spend *= 1 + increase

print(month)  # 8

