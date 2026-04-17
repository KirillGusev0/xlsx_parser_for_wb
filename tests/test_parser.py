import pytest
from app.parser import parse_products


@pytest.mark.asyncio
async def test_parse_products():
    products = await parse_products()
    assert isinstance(products, list)
    assert len(products) > 0

    sample = products[0]
    assert "Название" in sample
    assert "Цена" in sample
