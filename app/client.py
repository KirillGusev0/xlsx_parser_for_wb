import aiohttp
import asyncio
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Connection": "keep-alive",
    "Origin": "https://www.wildberries.ru",
    "Referer": "https://www.wildberries.ru/",
}


class WBClient:
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=HEADERS)
        return self

    async def __aexit__(self, *args):
        await self.session.close()

    async def fetch(self, url, params=None):
        async with self.session.get(url, params=params) as resp:
            resp.raise_for_status()

            text = await resp.text()

            try:
                return json.loads(text)
            except json.JSONDecodeError:
                print("WB вернул не JSON:")
                print(text[:500])
                return {}

    async def get_search_page(self, query, page):
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

        return await self.fetch(url, params)

    async def get_product_detail(self, nm_id):
        url = f"https://card.wb.ru/cards/detail?nm={nm_id}"
        return await self.fetch(url)
