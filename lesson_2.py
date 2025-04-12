import time
from lesson_2_data import courts

a = 0

while True:
    a += 1
    if a % 2 != 0:
        continue
    elif a > 20:
        break
    else:
        print('a =', a)

print('end of while cycle')

connected = False

a, b = 10, 15

names = []
for court in courts:
    names.append(court['court_name'])

names = [court['court_name'] for court in courts]


court_mapping = {court['court_code']: court['court_name'] for court in courts}
court_set = {court['court_name'] for court in courts}

print(court_mapping)

print('end of for cycle')
