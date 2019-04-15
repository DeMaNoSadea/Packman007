import json
import requests
import re
s = json.loads(str((requests.get('https://beloborod.ru/keksik.php').text)))


input('Нажмите Enter')
print(s)
input('Нажмите Enter')


def Dsum(dic, sum=0):
    if len(list(filter(lambda i: type(i) == str, list(dic.values())))) == 0:
        print("Нет чисел")
    else:
        for i in dic.values():
            if isinstance(i, int):
                sum += i
        return sum


print((Dsum(s)))
input('Нажмите Enter')


def Rlist(dic: dict):
    x = []
    for k in dic.keys():
        if re.match("text", k):
            x.append(dic.get(k))
    print(x)


Rlist(s)
input('Нажмите Enter')


def Rdict(d: dict):
    dc = d.copy()
    for key in list(dc.keys()):
        if re.match("text", key):
            dc.pop(key)
        else:
            pass
    print(dc)


Rdict(s)
input('Нажмите Enter, чтобы завершить')