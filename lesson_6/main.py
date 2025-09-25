import json
import requests



cbr_url = "https://cbr.ru/"

nasdaq_base_url = ""

def get_cbr():
    r = requests.get(cbr_url)

def get_nasdaq():

    headers = {
    "Host": "api.nasdaq.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:143.0) Gecko/20100101 Firefox/143.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.nasdaq.com/",
    "Origin": "https://www.nasdaq.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",
    }

    route = "https://api.nasdaq.com/api/quote/watchlist?symbol=comp|index&type=Rv"
    r = requests.get(route, headers=headers)
    data = r.json()

    pass


def get_kad():

    url = "https://kad.arbitr.ru/Kad/SearchInstances"
    header = {

        "Host": "kad.arbitr.ru",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "x-date-format": "iso",
        "Origin": "https://kad.arbitr.ru",
        "Connection": "keep-alive",
        "Referer": "https://kad.arbitr.ru/",
        "Cookie": "__ddg1_=QePZvb4aUiA0lYMMyoeO; CUID=26c0f73c-7f49-4669-9af9-75c2ec26e17b:DsZvK/so8MqOJfaJDWHqbA==; _ga=GA1.2.1362096996.1757771268; tmr_lvid=c5763f40b5d3dbbb0d68d50a02eba0c7; tmr_lvidTS=1745003823515; _ym_uid=1745003824584548367; _ym_d=1757771268; domain_sid=BjP8471q8kuFkraQC-2KE%3A1758212346421; _ga_Q2V7P901XE=GS2.2.s1758212345$o2$g0$t1758212345$j60$l0$h0; _ga_9582CL89Y6=GS2.2.s1758212345$o2$g0$t1758212345$j60$l0$h0; pr_fp=939128a6353ea3b26ff1c37adaf38372117e72430013d97a4524ec6aad8a9070; rcid=46d9069f-ecaa-403d-946a-263da3fa38d1; ASP.NET_SessionId=kjnk0l2voikhc55qglropjgv; __ddg8_=9jcQdM7m86kb9i6U; __ddg10_=1758212357; __ddg9_=46.138.253.202; _gid=GA1.2.1400921979.1758212345; _gat=1; _gat_FrontEndTracker=1; _ym_isad=2; tmr_detect=0%7C1758212347592; wasm=5ff2193ea62d3d246baf11b36b66b3da",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"

    }
    json = '{"Page":1,"Count":25,"Courts":[],"DateFrom":null,"DateTo":null,"Sides":[{"Name":"7701272485","Type":-1,"ExactMatch":false}],"Judges":[],"CaseNumbers":[],"WithVKSInstances":false}'
    r = requests.post(url, json=json)
    pass


def get_casestatus():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:143.0) Gecko/20100101 Firefox/143.0",
        # "Accept": "*/*",
        # "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        # "Accept-Encoding": "gzip, deflate, br, zstd",
        # "Content-Type": "application/json",
    }
    url = "https://www.casestatusext.com/cases/IOE0932447764"
    r = requests.get(url, headers=headers)

    pass


def get_roszdrav():

    url = 'https://roszdravnadzor.gov.ru/ajax/services/licenses'
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Cookie": "sputnik_session=1758213616117|1; uid=5575297789214627586",
        "Referer": "https://roszdravnadzor.gov.ru/",
        "Origin": "https://roszdravnadzor.gov.ru"
    }
    data = {
        "q_no": "Л041-00110-77/00576772"
    }
    j = json.dumps(data)
    # data = "draw=2&columns%5B0%5D%5Bdata%5D=col1.label&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=col2.label&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=col3.label&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=col4.label&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=col5.label&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=col6.label&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=col7.label&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=col8.label&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=col9.label&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=col10.label&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=false&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=col11.label&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=col12.label&columns%5B11%5D%5Bname%5D=&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=false&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B12%5D%5Bdata%5D=col13.label&columns%5B12%5D%5Bname%5D=&columns%5B12%5D%5Bsearchable%5D=true&columns%5B12%5D%5Borderable%5D=false&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=col14.label&columns%5B13%5D%5Bname%5D=&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=false&columns%5B13%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D=col15.label&columns%5B14%5D%5Bname%5D=&columns%5B14%5D%5Bsearchable%5D=true&columns%5B14%5D%5Borderable%5D=false&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B15%5D%5Bdata%5D=col16.label&columns%5B15%5D%5Bname%5D=&columns%5B15%5D%5Bsearchable%5D=true&columns%5B15%5D%5Borderable%5D=false&columns%5B15%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B15%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B16%5D%5Bdata%5D=col17.label&columns%5B16%5D%5Bname%5D=&columns%5B16%5D%5Bsearchable%5D=true&columns%5B16%5D%5Borderable%5D=false&columns%5B16%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B16%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B17%5D%5Bdata%5D=col18.label&columns%5B17%5D%5Bname%5D=&columns%5B17%5D%5Bsearchable%5D=true&columns%5B17%5D%5Borderable%5D=false&columns%5B17%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B17%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B18%5D%5Bdata%5D=col19.label&columns%5B18%5D%5Bname%5D=&columns%5B18%5D%5Bsearchable%5D=true&columns%5B18%5D%5Borderable%5D=false&columns%5B18%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B18%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=25&search%5Bvalue%5D=&search%5Bregex%5D=false&prev_total=0&q_no=%D0%9B041-00110-77%2F00576772&q_registry=0&q_type=1&q_region=&dt_from=&dt_to=&q_org_inn=&q_activity=&q_active=0&q_org_ogrn=&q_org_label="

    r = requests.post(url, json=j)
    pass

def main():
    # get_cbr()
    # get_nasdaq()
    # get_kad()
    # get_casestatus()
    get_roszdrav()

if __name__ == "__main__":
    main()
