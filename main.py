y = input("Введите количество билетов:")
chek = int(y)
chek_tickets = []
summ_tickets = []
age_list = []
summ1 = 0
age_summ1 = [0, 17]
summ2 = 990
age_summ2 = [18, 24]
summ3 = 1390
age_summ3 = [25, 100]
for i in range(1, chek + 1):
    chek_tickets = list(range(1, chek + 1))
c = int(len(chek_tickets))
for i in range(c):
    x = int(input("Введите возраст посетителя: "))
    age_list.append(x)
    if x >= age_summ1[0] and x <= age_summ1[1]:
        summ_tickets.append(summ1)
    elif x >= age_summ2[0] and x <= age_summ2[1]:
        summ_tickets.append(summ2)
    elif x >= age_summ3[0] and x <= age_summ3[1]:
        summ_tickets.append(summ3)
if c > 3:
    print("Сумма вашего заказа", float(sum(summ_tickets) * 0.9), "руб.")
else:
    print("Сумма вашего заказа:", sum(summ_tickets), "руб.")
