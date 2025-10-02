import time
import requests
from datetime import date, timedelta
from bs4 import BeautifulSoup
import traceback


class CBRCurrencyParser:

    BASE_URL = 'https://cbr.ru'

    def __init__(self):
        """
        Data available from 01.07.1992

        """
        pass

    def get_cbr_soup(self, date):
        url = f"{self.BASE_URL}/currency_base/daily/?" \
              f"UniDbQuery.Posted=True&" \
              f"UniDbQuery.To={date}"
        for _ in range(5):
            try:
                r = requests.get(url, timeout=5)
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

    def parse_cbr_soup(self, soup):
        rows = soup.find('table').find_all('tr')
        for row in rows:
            data = row.find_all('td')
            if data:
                ticker = data[1].text
                value = data[4].text
                if ticker == 'USD':
                    return value


    def start(self):
        data = []
        today = date.today()
        parse_date = date(year=2020, month=9, day=24)
        while parse_date <= today:

            parse_date_str = parse_date.strftime('%d.%m.%Y')
            soup = self.get_cbr_soup(parse_date_str)
            if soup:
                ccy_value = self.parse_cbr_soup(soup)
                data.append((parse_date.isoformat(), ccy_value))

                print(f'Курс USD на дату {parse_date_str} --- {ccy_value} RUB')
                parse_date = parse_date + timedelta(days=1)



def main():
    parser = CBRCurrencyParser()
    parser.start()


if __name__ == "__main__":
    main()