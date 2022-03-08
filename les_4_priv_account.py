import datetime
from functools import reduce

def add_loss(private_account):
    global sum_amount
    loss = float(input("Введите сумму расхода: "))
    if loss > sum_amount:
        print('Сумма расхода превышает сумму счета!')
    else:
        name_loss = input('Введите наименование покупки: ')
        sum_amount -= loss
        private_account.update([([str(datetime.datetime.now()), ["покупка: "+ name_loss, loss]])])

def add_profit(private_account):
    global sum_amount
    profit = float(input("Введите сумму пополнения счета: "))
    sum_amount += profit
    private_account.update([([str(datetime.datetime.now()), ["пополнение счета", profit]])])


def view_history(private_account):
    list_dat_oper = sorted(private_account.keys())
    for oper in list_dat_oper:
        # detal_f = lambda d_oper: d_oper += ' ' + list_dat_oper
        print('Дата операции: ' + oper, reduce(lambda x,y: str(x) + ' ' + str(y), private_account[oper]).strip())

private_account = {}
sum_amount = float(0)

while True:
    oper = input("Введите операцию (0 - приход, 1 - расход, 2 - показать историю, Enter или любое другой символ - выход): ")
    if oper == '0':
        add_profit(private_account)
    elif oper == '1':
        add_loss(private_account)
    elif oper == '2':
        view_history(private_account)
    else:
        break
