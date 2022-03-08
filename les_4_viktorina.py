one_to_nineteen = ('', u'первое', u'второе', u'третье', u'четвертое', u'пятое', u'шестое', u'седьмое', u'восьмое', u'девятое',
                   u'десятое', u'одиннадцатое', u'двенадцатое', u'тринадцатое', u'четырнадцатое', u'пятнадцатое',
                   u'шестнадцатое', u'семнадцатое', u'восемьнадцатое', u'девятьнадцатое', u'тридцатое')

decs = ('', '', u'двадцать', u'тридцать')


def _one_convert(int_data):
    return one_to_nineteen[int_data]

def _two_convert(int_data, str_data):
    if int_data in range(20):
        result = one_to_nineteen[int_data]
    elif int_data == 30:
        result = one_to_nineteen[20]
    else:
        result = decs[int(str_data[0])]

        if str_data[1] != '0':
            result = u'%s %s' % (result, one_to_nineteen[int(str_data[1])])

    return result

def convert_data(str_data):
    length = len(str_data)
    int_data = int(str_data)

    if length == 1:
        result = _one_convert(int_data)

    else:
        result = _two_convert(int_data, str_data)


    return result.strip()


def conver_month(num_month):
    dict_month = {1:'января', 2:'февраля', 3:'марта',
                  4: 'апреля', 5: 'мая', 6: 'июня',
                  7: 'июля', 8: 'августа', 9: 'сентября',
                  10: 'октября', 11: 'ноября', 12: 'декабря'}
    return dict_month[num_month]


dict_famos = {
            'person_1': {'name': 'Путина Владимира Владимировича', 'bithday': '07.10.1952'},
            'person_2': {'name': 'Ленина Владимира Ильича', 'bithday': '22.04.1870'},
            'person_3': {'name': 'Гагарина Юрия Алексеевича', 'bithday': '09.03.1934'},
            'person_4': {'name': 'Менделеева Дмитрия Ивановича', 'bithday': '08.02.1834'},
            'person_5': {'name': 'Гоголя Николая Васильевича', 'bithday': '19.03.1809'}
            }

correct_answer = []
error_answer = []

print('Необходимо указать дату рождения указанного лица в формате dd.mm.yyyy (для чисел меньше 10 указывать лидирующий 0)')
print('дату 4 апреля 1979 года надо ввести 04.04.1979')
print('-------------------------------------------------')
for i in dict_famos.keys():
    fio = dict_famos[i]['name']
    in_data = input(f"Введите дату рождения {fio}: ")
    correct_data = dict_famos[i]['bithday']
    if in_data == correct_data:
       correct_answer.append(1)
       # разберем дату
       data_bithday = in_data[:2]
       month_bithday = in_data[3:5]
       year_bithday = in_data[6:10]
       print(convert_data(data_bithday), conver_month(int(month_bithday)), year_bithday, 'года')
    else:
        error_answer.append(1)

print('Правильных ответов:',  sum(correct_answer))
print('Количество ошибок:',  sum(error_answer))
print('Процент правильных ответов:', round(sum(correct_answer) / len(dict_famos), 2)*100, ' %')