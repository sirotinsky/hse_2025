# from queue import Queue
#
# array = [[1,2],
#          [3,4],
#          [5,6]]
#
# array[0][2]

import datetime

import time
import random

#
# random.shuffle(array)
#
# start_time = time.time()
# if 99999 in array:
#     print('Found')
# end_time = time.time()
#
# print(f'Done in {end_time-start_time} secs')


a = list(range(1000000000))

value = 99999

low = 0
cycle_count = 0
high = len(a) - 1
mid = len(a) // 2
start_time = time.time()
while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
    cycle_count += 1
end_time = time.time()

print(f'Done in {end_time-start_time} secs')
print(f'Cycles {cycle_count}')

if low > high:
    print('No value')
else:
    print('ID =', mid)



pass

# hash_map = {}
# hash_map['kirill'] = '32'
# hash_map['alena'] = '24'


# q = Queue()
#
# stack = list()
#
# stack.append(1)
# print(stack)
# stack.append(2)
# print(stack)
# stack.append(3)
# print(stack)
# stack.pop()
# print(stack)



# a = []
# for i in range(10):
#     a.append(randint(1, 50))
# a.sort()
# print(a)

# искомое число
value = int(input())

# индексы первого элемента, последнего и среднего
low = 0
high = len(a) - 1
mid = len(a) // 2

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print('No value')
else:
    print('ID =', mid)