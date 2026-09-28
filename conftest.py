import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    # Создаём новый экземпляр коллекции для каждого теста
    return BooksCollector()
