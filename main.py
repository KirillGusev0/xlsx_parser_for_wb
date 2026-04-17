import asyncio
from app.parser import parse_products
from app.exporter import save_all, save_filtered


async def main():
    products = await parse_products()
    save_all(products)
    save_filtered(products)


if __name__ == "__main__":
    asyncio.run(main())
