"""
This module is for something
"""
urls = [i for i in range(100)]

def get_data_from_web(url) -> dict:
    """
    This func is for http data requests
    :param url:
    :return:
    """
    data = {}

    return data


def normalize_data(data: dict) -> dict:
    nor_data = {}

    return nor_data

def save_to_db(data: dict) -> None:
    pass


def main():
    for url in urls:
        data = get_data_from_web(url)
        nor_data = normalize_data(data)
        save_to_db(nor_data)


if __name__ == "__main__":
    main()