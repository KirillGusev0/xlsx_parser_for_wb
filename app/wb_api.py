import requests

HEADERS = {"User-Agent": "Mozilla/5.0"}


def get_search_page(query, page):
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"

    params = {
        "appType": 1,
        "curr": "rub",
        "dest": -1257786,
        "page": page,
        "query": query,
        "resultset": "catalog",
        "sort": "popular",
        "spp": 30,
    }

    response = requests.get(url, params=params, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def get_product_detail(nm_id):
    url = f"https://card.wb.ru/cards/detail?nm={nm_id}"

    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
