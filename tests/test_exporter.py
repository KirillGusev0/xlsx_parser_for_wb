from app.exporter import save_all


def test_export():
    data = [{"Название": "Тест", "Цена": 1000, "Рейтинг": 5, "Страна": "Россия"}]

    save_all(data)
