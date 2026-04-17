import asyncio
from app.config import QUERY, PAGES, CONCURRENT_REQUESTS
from app.client import WBClient
import random


async def parse_products():
    products = []

    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    async with WBClient() as client:
        for page in range(1, PAGES + 1):
            data = await client.get_search_page(QUERY, page)
            items = data.get("data", {}).get("products", [])

            tasks = [parse_product(client, item, semaphore) for item in items]

            results = await asyncio.gather(*tasks)
            products.extend(results)

    return products


async def parse_product(client, item, semaphore):

    await asyncio.sleep(random.uniform(0.3, 1.2))
    async with semaphore:
        nm_id = item.get("id")

        try:
            detail = await client.get_product_detail(nm_id)
            product_data = detail.get("data", {}).get("products", [{}])[0]
        except:
            product_data = {}

        characteristics = product_data.get("options", [])
        characteristics_dict = {c.get("name"): c.get("value") for c in characteristics}

        images = item.get("pics", [])
        image_links = [
            f"https://images.wbstatic.net/c246x328/new/{img}.jpg" for img in images
        ]

        sizes = [s.get("name") for s in item.get("sizes", [])]

        result_dec = {
            "Ссылка": f"https://www.wildberries.ru/catalog/{nm_id}/detail.aspx",
            "Артикул": nm_id,
            "Название": item.get("name"),
            "Цена": item.get("salePriceU", 0) / 100,
            "Описание": product_data.get("description", ""),
            "Изображения": ", ".join(image_links),
            "Характеристики": str(characteristics_dict),
            "Продавец": product_data.get("supplier", ""),
            "Ссылка на продавца": f"https://www.wildberries.ru/seller/{product_data.get('supplier','')}",
            "Размеры": ", ".join(filter(None, sizes)),
            "Остатки": item.get("totalQuantity", 0),
            "Рейтинг": item.get("reviewRating", 0),
            "Отзывы": item.get("feedbacks", 0),
            "Страна": characteristics_dict.get("Страна производства", ""),
        }
        return result_dec
