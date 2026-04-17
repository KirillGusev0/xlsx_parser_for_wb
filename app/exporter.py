import pandas
from app.config import OUTPUT_ALL, OUTPUT_FILTERED, MIN_RATING, MAX_PRICE, COUNTRY


def save_all(products):
    df = pandas.DataFrame(products)
    df.to_excel(OUTPUT_ALL, index=False)


def save_filtered(products):
    df = pandas.DataFrame(products)

    filtered = df[
        (df["Рейтинг"] >= MIN_RATING)
        & (df["Цена"] <= MAX_PRICE)
        & (df["Страна"] == COUNTRY)
    ]

    filtered.to_excel(OUTPUT_FILTERED, index=False)
