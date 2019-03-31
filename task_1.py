import requests
import json
import re


input('Enter')
r = json.loads(str((requests.get('https://beloborod.ru/keksik.php').text)))
print(r)

input('Enter')

def dicsum(dic, sum=0):
    if len(list(filter(lambda i: type(i) == str, list(dic.values())))) == 0:
        print("Нет элементов с числовым значением")
    else:
        for i in dic.values():
            if isinstance(i, int):
                sum += i
        return sum

print((dicsum(r)))
input('Enter')

def reglist(dic: dict):
    z = []
    for key in dic.keys():
        if re.match("text", key):
            z.append(dic.get(key))
    print(z)

reglist(r)
input('Enter')

def regdict(d: dict):
    dic = d.copy()
    for key in list(dic.keys()):
        if re.match("text", key):
            dic.pop(key)
        else:
            pass
    print(dic)
regdict(r)

