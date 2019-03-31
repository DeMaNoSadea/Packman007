##Task 1
def count_sheep(array1):
    sheep = 0
    for x in array1:
        if x == True:
            sheep += 1
    print("Task 1:  ", sheep)
    return sheep


d = [True, True, True, False, True, True, True, True, True, False, True, False,
     True, False, False, True,
     True, True, True, True,
     False, False, True, True]
count_sheep(d)


##Task 2
def digit(n):
    return [int(s) for s in str(n)[::-1]]


print("Task 2:  ", digit(348597))


##Task 3
def manipulate_data(data):
    positive_count = 0
    negative_sum = 0
    for n in data:
        if n > 0:
            positive_count += 1
        elif n < 0:
            negative_sum += n
    return [positive_count, negative_sum]


print("Task 3:  ", manipulate_data([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))


##Task 4
def squareSum(numbers):
    return sum(x ** 2 for x in numbers)


print("Task 4:  ", squareSum([1, 2, 2]))


##Task 5
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


print("Task 5:  ", count_by(3, 10))


##Task 6
def square_or_square_root(arr):
    return [i ** 0.5 if (i ** 0.5).is_integer() else i ** 2 for i in arr]


print("Task 6:  ", square_or_square_root([4, 3, 9, 7, 2, 1]))


# Task 7
def multiList(List):
    res = 1
    for x in List:
        res = res * x
    print("Task 7:  ", res)
    return res


multiList([1, 2, 3, 4])


##Task 8
def lists(my_list):
    del my_list[1::2]
    print("Task 8:  ", my_list)
    return my_list


lists(['Keep', 'Remove', 'Keep', 'Remove', 'Keep'])


##Task 9
def MArray(arr1, arr2):
    return sorted(set(arr1 + arr2))


arr1 = [1, 3, 5, 7, 9]
arr2 = [10, 8, 6, 4, 2]
print("Task 9:  ", MArray(arr1, arr2))


##Task 10
def exam(arry1, arry2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arry1, arry2) if b))


print("Task 10: ", exam(['a', 'a', 'b', 'b'], ['a', 'c', 'b', 'd']))


##Task 11
def multiple_index(l):
    return [l[i] for i in range(1, len(l)) if l[i] % i == 0]


print("Task 11: ", multiple_index([68, -1, 1, -7, 10, 10]))


##Task 12
def ad_leght(srg):
    return ["{} {}".format(i, len(i)) for i in srg.split(' ')]


print("Task 12: ", ad_leght('apple ban'))


##Task 13
def divi_by(numd, divisor):
    return [x for x in numd if x % divisor == 0]


print("Task 13: ", divi_by([1, 2, 3, 4, 5, 6, 7, 8], 2))


##Task 14
def Rev(rever_list):
    rever_list.reverse()
    print("Task 14: ", rever_list)
    return rever_list


rever_list = [4, 5, 1, 3]
Rev(rever_list)


##Task 15
def two_hig(ls):
    return False if isinstance(ls, str) else sorted(set(ls), reverse=True)[0:2]


print("Task 15: ", two_hig([4, 10, 10, 9]))


##Task 16
def even_odd(i):
    if i % 2 == 0 :
        print("Task 16:  Even")
    else:
        print("Task 16:  Odd")


even_odd(54)


##Task 17
def Nagative(num):
    return -abs(num)


print("Task 17: ", Nagative(45))


##Task 18
def solut(arr):
    arr.sort()
    return arr[0]


print("Task 18: ", solut([-34, 1511, -5, -2, 0]))


##Task 19
def nonsum(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


print("Task 19: ", nonsum([6, 2, 1, 8, 10]))


##Task 20
def invertor(num):
    return [-x for x in num]


print("Task 20: ", invertor([1, 2, -3, 4, 5, -7]))


##Task 21
def bmi(weight, height):  ## height - в метрах
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"


print("Task 21: ", bmi(80, 2))


##Task 22
def plus_arr(arrr1, arrr2):
    return sum(arrr1 + arrr2)


print("Task 22: ", plus_arr([1, 1, 1, 1], [1, 1, 1, 1]))


##Task 23
def oddCount(n):
    return n // 2


print("Task 23: ", oddCount(15))


##Task 24
def no_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0


print("Task 24: ", no_zeros(1450580))


##Task 25
def remove_duplicates(numbers):
    newlist = []
    for number in numbers:
        if number not in newlist:
            newlist.append(number)
    return newlist


print("Task 25: ", remove_duplicates([1, 2, 3, 4, 5, 5, 5, 6, 3, 2, 5, 99, 1, 1, 1, 1, 4, 5, 6]))
