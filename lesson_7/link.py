import json
import requests

headers = {
'Host': 'linkmark.ru',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:144.0) Gecko/20100101 Firefox/144.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '276',
'Origin': 'https://linkmark.ru',
'Connection': 'keep-alive',
'Referer': 'https://linkmark.ru/request/cDZxT0lORnNwMGJma3ZQTUpyVUhYUT09?new=1',
# 'Cookie': 'XSRF-TOKEN=eyJpdiI6IkkwV054XC9qSlVjajJGUjNTdXZhTGxnPT0iLCJ2YWx1ZSI6InYyVlAzMFdcL3J6TXNHK1B3XC96YkV6VTZUV0hEYmhcL0h0MlhiSUtsSGJlMjlNTUZzT2tsTWZCa2RpTlwvdUhnNFVtSmxGS3FFN256N21VTmI5TW9ZNVd4QT09IiwibWFjIjoiMzQ0ODJmYThmYTIwYWQyYmJiZTU3ZjZmODcwNzkwNjAxMTM2ZTFlMjUzNWQwOTg2M2YzOGQzOWYxMGU5YTFlMyJ9; laravel_session=eyJpdiI6IkthMkFNM2FFcVZRekxsekUranlvZFE9PSIsInZhbHVlIjoiOU9RQ3hLWUhsN29PdFdWTWpwdFZhOVFmSUQ2ckRlZkNPaHdxdzJCK0dtR0VIR3hCRllLV0kydVViZWZHc0VhOWxwbkZDM1YzbFUxOWd1OUVhYkFXdXc9PSIsIm1hYyI6Ijk5YjhmZDY0NGY2MmI1YjVkOTkxZDAxMGVhNDNmOTQ0ZTIwY2I3YjA0YzkyMmY4ZDY0MDFhYzZlYWE3Mzc2MTgifQ%3D%3D; _ym_uid=1760634137675062073; _ym_d=1760634137; _ga=GA1.2.2104216171.1760634137; _gid=GA1.2.500483084.1760634137; _ga_HRGM8PVJ6P=GS2.2.s1760634136$o1$g1$t1760634188$j8$l0$h0; _ym_isad=2',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
}
data = {
'search':	"Сиротинский",
'search_2':	"",
'vena-class':	"Выбрать",
'search_4':	["", ""],
'mktu4[]':	"",
'vena_limit_subclass':	"0",
'vena_limit_heading':	"12",
'search_type':	"1",
'_token':	"Lx1pJ32oeGsMYg56u5MK5iYvVupHycYCIU4gswFR"
}

def get_web():
    url = 'https://linkmark.ru/search'

    r = requests.post(url, data=json.dumps(data))

    pass

def main():
    get_web()

if __name__ == "__main__":
    main()