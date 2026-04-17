# xlsx_parser_for_wb

# WB Parser

Сервис для парсинга каталога товаров с Wildberries по поисковому запросу с последующим сохранением данных в XLSX.

---

## Возможности:

- асинхронный парсинг каталога товаров  
- сбор данных по каждому товару (карточка + список)  
- обработка большого количества товаров (async + concurrency)  
- защита от нестабильного API (fallback через text → json)  
- фильтрация товаров по условиям (рейтинг, цена, страна)  
- экспорт данных в XLSX (полный каталог + отфильтрованный)  
- базовая защита от антибота (headers + delay)  
- покрытие базовыми тестами (pytest)  

---

## Основные компоненты:

### parser:
- получает список товаров по поисковому запросу  
- обходит пагинацию  
- асинхронно собирает данные карточек товаров  
- нормализует данные (изображения, размеры, характеристики)  
- возвращает список товаров  

---

### client:
- выполняет HTTP-запросы к API Wildberries  
- обрабатывает нестандартные ответы (text/plain вместо JSON)  
- инкапсулирует работу с сетью  

---

### exporter:
- сохраняет полный каталог в XLSX  
- применяет фильтрацию:
  - рейтинг ≥ 4.5  
  - цена ≤ 10000  
  - страна производства = Россия  
- сохраняет отфильтрованные данные в отдельный файл  

---

## Локальный запуск:

```bash
git clone https://github.com/KirillGusev0/xlsx_parser_for_wb.git
cd xlxs_parser_wb

python3 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python main.py
```
data/wb_catalog.xlsx — полный каталог
data/wb_filtered.xlsx — отфильтрованные товары
Запуск тестов:
```bash
pytest -v
```

Запуск через Docker:
```bash
docker compose up --build
```
После выполнения:

результаты появятся в папке data/

Запуск тестов в Docker:
```bash
docker compose run --rm tests
```
Конфигурация:

Основные параметры задаются в app/config.py:

QUERY — поисковый запрос
PAGES — количество страниц
CONCURRENT_REQUESTS — уровень параллелизма
MIN_RATING, MAX_PRICE, COUNTRY — параметры фильтрации
