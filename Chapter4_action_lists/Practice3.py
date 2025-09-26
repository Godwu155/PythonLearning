import time

numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

for number in numbers:
    print(number)

numbers = []

Num = [value ** 3 for value in range(1, 11)]
print(Num)


def get_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time


# get_time()
# print(get_time())
N1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = []
N2 = [value ** 3 for value in N1]
print(N2)
