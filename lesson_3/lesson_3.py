import csv
import json
from decimal import Decimal
from time import time
from datetime import datetime, date, timedelta
import re
import os
from dadata import Dadata


DADATA_API_KEY = '340e9972893243b9ef326fb473a3fb3b2ccf3bdd'
DADATA_SECRET_KEY = '5a78e67c65c44d1051aed5f3e51e9f9014ea7bdc'
ddt = Dadata(DADATA_API_KEY, DADATA_SECRET_KEY)

a = ddt.find_by_id('party', '7701272485')
print(a)



BASE_DIR = os.path.dirname(__file__)
abs_path = os.path.join(BASE_DIR, '1000_efrsb_messages.json')
efrsb_path = '1000_efrsb_messages.json'
traders_csv_path = os.path.join(BASE_DIR, 'traders.csv')


today = datetime.now()

due_term = 14
action_date = datetime(2025, 4, 5, 1, 1)

if action_date > (today - timedelta(days=due_term)):
    print("Срок не пропущен")
else:
    print("Срок пропущен")


print(today)
a = {'full_name': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ТОРГОВЫЙ ПАРТНЁР"',
      'short_name': 'ООО "ТОРГОВЫЙ ПАРТНЁР"',
      'inn': '6732101128',
      'ogrn': '1156733001424',
      'region': 'Смоленская область',
      'category': 'Обычная организация',
      'category_code': 'SimpleOrganization',
      'bankruptcy_id': '183678',
      'case_number': 'А62-10312/2017',
      'creation_date': today,
      'address': '214012, Смоленская обл, г Смоленск, ул Кашена, д 1, офис 719'}

# with open('test.json', 'w') as f:
#     json.dump(a, f, ensure_ascii=False)

price_1 = Decimal(str(12.02)).__round__(4)
price_2 = Decimal(str(11.01))
total = price_1 + price_2
print(total)




def main():
    start_time = time()
    result = set()
    with open('/Users/kirill/git/hse_2025/lesson_3/1000_efrsb_messages.json', 'r') as f:
        data = json.load(f)

    pattern = r'\b\d{10}\b'
    for i in data:
        a = re.findall(pattern, i['msg_text'])
        if a:
            for y in a:
                result.add(y)
    end_time = time()
    print(f'Выполнено за {end_time - start_time} сек')


if __name__ == "__main__":
    main()


