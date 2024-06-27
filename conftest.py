import pytest

from main import BooksCollector

# создание объекта класса


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector
