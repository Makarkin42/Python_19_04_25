import random
import time

spisok = [random.randint(1, 100) for i in range(50000)]
#clean = sorted(spisok, reverse=True)
'''#print(clean.reverse())
#print(clean[::-1])

spisok.sort()
#print(spisok)'''

def selectionsort(listik):
    timer = time.time()
    listik = listik[:]
    for i in range(len(listik) - 1):
        smallest_ind = i
        for a in range(i + 1, len(listik)):
            if listik[a] > listik[smallest_ind]:
                smallest_ind = a
        if smallest_ind != i:
            listik[i], listik[smallest_ind] = listik[smallest_ind], listik[i]
    newtime = time.time()
    final = newtime - timer
    #print(final)
    return listik

#print(spisok[:20])
#selectionsort(spisok)

def bingosort(listik):
    timer = time.time()
    listik = listik[:]
    index = 0
    bingo = listik[index]
    maxnum = bingo
    for i in range(len(listik)):
        if listik[i] < bingo:
            bingo = listik[i]
        if listik[i] > maxnum:
            maxnum = listik[i]
    nextbingo = maxnum
    while index < len(listik) - 1 and nextbingo != bingo:
        for i in range(index, len(listik)):
            if listik[i] == bingo:
                listik[i], listik[index] = listik[index], listik[i]
                index += 1
            if listik[i] < nextbingo and listik[i] != bingo:
                nextbingo = listik[i]
        bingo = nextbingo
        nextbingo = maxnum
    newtime = time.time()
    final = newtime - timer
    #print(final)
    return listik
#print(spisok[:20])

#bingosort(spisok)


def pancakesort(listik):
    timer = time.time()
    if len(listik) > 1:
        for i in range(len(listik), 1, -1):
            maxind = 0
            for a in range(i):
                if listik[a] > listik[maxind]:
                    maxind = a
            if maxind < i:
                listik[:maxind+1] = listik[:maxind+1][::-1]
                listik[:i] = listik[:i][::-1]
    newtime = time.time()
    final = newtime - timer
    #print(final)
    return listik
#print(spisok[:20])
#pancakesort(spisok)

def insertionsort(listik):
    timer = time.time()
    listik = listik[:]
    for i in range(1, len(listik)):
        for a in range(i, 0, -1):
            if listik[a] < listik[a - 1]:
                listik[a], listik[a-1] = listik[a-1], listik[a]
            else:
                break
    final = time.time()
    #print(final - timer)
    return listik
#insertionsort(spisok)

def bubblesort(listik):
    timer = time.time()
    listik = listik[:]
    for i in range(len(listik) - 1):
        for a in range(len(listik) - i - 1):
            if listik[a] > listik[a+1]:
                listik[a], listik[a - 1] = listik[a - 1], listik[a]
    final = time.time()
    #print(final - timer)
    return listik
#bubblesort(spisok)

def merge(listik1, listik2):
    res = []
    index1 = 0
    index2 = 0
    while index1 < len(listik1) and index2 < len(listik2):
        if listik1[index1] < listik2[index2]:
            res.append(listik1[index1])
            index1 += 1
        else:
            res.append(listik2[index2])
            index2 += 1
    res += listik1[index1:] + listik2[index2:]
    return res

def mergesort(listik):
    center = len(listik) // 2
    left, right = listik[:center], listik[center:]
    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)
    return merge(left, right)
#print(spisok)
timer = time.time()
mergesort(spisok)
final = time.time()
print(final - timer)

def randomlist(listik:list):
    if len(listik) < 100:
        listik.append(random.randint(1, 100))
        listik = randomlist(listik)
    return listik
#print(randomlist(listik=[]))
#print(mergesort(randomlist(listik=[])))

def quicksort(listik):
    if len(listik) > 1:
        pivot = random.choice(listik)
        left = [num for num in listik if num < pivot]
        right = [num for num in listik if num > pivot]
        mid = [num for num in listik if num == pivot]
        listik = quicksort(left) + mid + quicksort(right)
    return listik
timer = time.time()
quicksort(spisok)
final = time.time()
print(final - timer)