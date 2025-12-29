#from numba import njit


def fibonach1(n):
    if n in (1, 2):
        return 1
    return fibonach1(n - 1) + fibonach1(n - 2)

#print(fibonach1(10))

def fibo(n):
    listik = []
    for i in range(n):
        if len(listik) < 2:
            listik.append(int(1))
        else:
            listik.append(listik[-1] + listik[-2])
    return listik[-1]

print(fibo(100))