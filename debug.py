import random

def randomer():
    return int(random.randint(1, 1000))

def start():
    counter = []
    for i in range(100000):
        counter.append(randomer())
    return counter  # breakpoint

def analyze():
    data = start()  # Поставим ТОЧКУ ОСТАНОВА
    ll = len(data)  # breakpoint
    data = [u for u in data if u % 10 == 7]  # breakpoint
    print(len(data) / ll * 100)  # breakpoint

if __name__ == "__main__":
    analyze()