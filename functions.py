import math

#Функции
def Counter(s, f, t, flag=1):
    s = int(s)
    f = int(f)
    t = int(t)
    lst = []
    if flag == 1:
        for i in range(s, f + 1, t):
            x = math.sin(i) + 0.1 * math.sin(i ** 5)
            lst.append(x)
    if flag == 2:
        for i in range(s, f + 1, t):
            x = math.cos(i) + 0.1 * math.cos(i ** 5)
            lst.append(x)
    if flag == 3:
        for i in range(s, f + 1, t):
            x = math.tan(i) + 0.1 * math.tan(i ** 7)
            lst.append(x)
    return lst

#Сглаживание
def Smt(array, k):
    smt = []
    for i in range(len(array)):
        smt.append(SmtFunc(array[:i + 1], k))
    return smt

def SmtFunc(array, k):
    while abs(array[-1] - (sum(array) / len(array))) / abs(array[-1]) > k:
        array.pop(0)
    element = sum(array) / len(array)
    return element

#Метод наименьших квадратов
def Mnk(array):
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    for i in range(len(array)):
        sum_x += i
        sum_x2 += i**2
        sum_y += array[i]
        sum_xy += i*array[i]
    a = (len(array)*sum_xy - sum_y*sum_x)/(len(array)*sum_x2 - sum_x**2)
    b = (sum_y - a*sum_x) / len(array)
    mnk = []
    for i in range(len(array)):
        x = a*i + b
        mnk.append(x)
    return mnk

def Aprk(array):
    p = len(array)
    if array != []:
        if p == 1:
            b = array[0]
        else:
            k = array[p-1] - array[p-2]
            b = array[p-1] - k*(p-1)
        x = k*p + b
        array.append(x)
        return array


