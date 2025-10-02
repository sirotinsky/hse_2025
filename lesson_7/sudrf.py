import time
import requests
import httpx
from datetime import date, timedelta
from bs4 import BeautifulSoup
import traceback


class CBRCurrencyParser:

    BASE_URL = 'https://kln--spb.sudrf.ru'
    HEADERS = {
        'Host': 'kln--spb.sudrf.ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:143.0) Gecko/20100101 Firefox/143.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        'Referer': 'https://kln--spb.sudrf.ru/modules.php?name=sud_delo',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
    }

    def __init__(self):
        pass

    def get_soup(self, date):
        url = f"{self.BASE_URL}modules.php?" \
              f"name=sud_delo&" \
              f"srv_num=1&" \
              f"H_date=18.09.2025"
        for _ in range(5):
            try:
                r = requests.get(url, headers=self.HEADERS)
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                return soup
            except requests.exceptions.ReadTimeout:
                print('Timeout exceeded')
                time.sleep(1)
                continue
            except Exception as exc:
                print(traceback.format_exception(exc))
                break

    def parse_soup(self, soup):
        pass


    def start(self):
        data = []
        today = date.today()
        parse_date = date(year=2020, month=9, day=24)
        while parse_date <= today:

            parse_date_str = parse_date.strftime('%d.%m.%Y')
            soup = self.get_soup(parse_date_str)
            if soup:
                result = self.parse_soup(soup)
                data.append((parse_date.isoformat(), result))

                print(f'Курс USD на дату {parse_date_str} --- {ccy_value} RUB')
                parse_date = parse_date + timedelta(days=1)



def main():
    parser = CBRCurrencyParser()
    parser.start()


if __name__ == "__main__":
    main()