import time
from traceback import format_exception
from lesson_2_data import respondents, courts

def gen_court_header(court: dict) -> str:
    header = f"В {court['court_name']}\n" \
         f"Адрес: {court['court_address']}\n"
    return header


def gen_respondent_header(respondent: dict) -> str:
    header = f"Ответчик: {respondent['short_name']}\n" \
             f"ИНН {respondent['inn']} ОГРН {respondent['ogrn']}\n" \
             f"Адрес: {respondent['address']}\n" \
             f"---------------"
    return header

def main():
    print('start')
    court_mapping = {i['court_code']: i for i in courts}
    for i in respondents:
        try:
            code = i['case_number'][:3]
            court = court_mapping[code]
            court_header = gen_court_header(court)
            print(court_header)
            respondent_header = gen_respondent_header(i)
            print(respondent_header)
        except Exception as exc:
            format_exception(exc)
            continue


if __name__ == "__main__":
    main()
    print('stop')
