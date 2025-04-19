'''line1 = input('Напиши первую строку\n')
line2 = input('Напиши вторую строку\n')
line = [line1, line2]
def our(line):
    general_line = ''
    for i in line:
        general_line += i + " "
    return general_line
print(our(line))'''

strocka = "Учебник, Город, Рюкзак, Одеяло, Змея"

def spisok(rewers):
    answer = rewers.split()
    answer.reverse()
    return answer[::-1]
print(spisok(strocka))