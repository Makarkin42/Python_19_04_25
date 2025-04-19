'''def square(a,b):
  answer = a*b
  return answer
print(square(7,28))'''

'''numbers = (100,350,23,63,4,8)
def even(chetn):
  answer = 0
  for i in chetn:
      if i %2 == 0:
          answer += 1
  return answer
print(even(numbers))'''

temp = [1, 1, 1, 1, 1, 3, 43, 43, 4, 3, 4, 9, 6, 7, 9, 7, 9, 5, 5, 5, 78, 9, 9, 9, 78, 6, 66, 6]
'''def cucle(spisok):
   otvet = []
   for i in spisok:
      if i not in otvet:
        otvet.append(i)
   return otvet
print(cucle(temp))'''

strocka = "Молоко окно шкатулка стол мама"
def bukvi(count):
    otvet = {}
    for i in count.lower():
      if i not in otvet:
         otvet[i] = 1
      else:
          otvet[i] += 1
    return otvet
print(bukvi(strocka))