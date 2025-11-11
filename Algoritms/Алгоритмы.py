import random

#spisok = [random.randint(1, 100) for i in range(10)]
spisok = [74, 92, 34, 89, 51, 80, 75, 1, 85, 3]
print(spisok)
#постоянная сложность   O(c)
def alg1(spisok):
    res = spisok[0]**2
    return res

#print(alg1(spisok))

#линейная сложность   O(n)   n = количество данных
def alg2(spisok):
    res = []
    for i in spisok:
        res.append(i**2)
    return res
#print(alg2(spisok))

#квадратичная сложность   O(n^2)
def alg3(spisok):
    res = []
    for i in spisok:
        for a in spisok:
            res.append((i, a))
    return res
print(alg3(spisok))

def test(n):
    a = 0
    for i in range(n):
        a *= n ** 2

    for n in range(a):
        for m in range(n):
            for z in range(m):
                p = a + z * m * n