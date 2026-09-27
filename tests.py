import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # Проверяем, что книги длиннее 40 символов не добавляются
    @pytest.mark.parametrize('book_name', ['а' * 41, 'б' * 50])
    def test_add_new_book_long_name_not_added(self, book_name):
        collector = BooksCollector()  # Создаём экземпляр класса

        collector.add_new_book(book_name)  # Пытаемся добавить длинное название

        assert book_name not in collector.get_books_genre()

    # Проверяем установку допустимого жанра для добавленной книги
    def test_set_book_genre_book_added_genre_set(self):
        collector = BooksCollector()
        book_name = 'Дюна'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')

        assert collector.get_book_genre(book_name) == 'Фантастика'

    # Проверяем, что для книги вне коллекции возвращается None
    def test_get_book_genre_book_not_added_return_none(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Несуществующая книга') is None

    # Проверяем получение книг по разным жанрам
    @pytest.mark.parametrize(
        'book_name, genre',
        [('Дюна', 'Фантастика'), ('Шерлок Холмс', 'Детективы')]
    )
    def test_get_books_with_specific_genre_book_with_genre_return_book(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_books_with_specific_genre(genre) == [book_name]

    # Проверяем получение текущего словаря книг и жанров
    def test_get_books_genre_two_books_added_return_dict(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')

        assert collector.get_books_genre() == {'Дюна': '', 'Оно': ''}

    # Проверяем, что книги с возрастным рейтингом не попадают в список для детей
    def test_get_books_for_children_books_with_age_rating_return_only_children_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_for_children() == ['Дюна']

    # Проверяем добавление существующей книги в избранное
    def test_add_book_in_favorites_book_added_add_to_favorites(self):
        collector = BooksCollector()
        book_name = 'Дюна'
        collector.add_new_book(book_name)

        collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books() == [book_name]

    # Проверяем, что одна книга не добавляется в избранное дважды
    def test_add_book_in_favorites_same_book_added_twice_one_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Дюна'
        collector.add_new_book(book_name)

        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books() == [book_name]

    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites_book_in_favorites_delete_book(self):
        collector = BooksCollector()
        book_name = 'Дюна'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        collector.delete_book_from_favorites(book_name)

        assert collector.get_list_of_favorites_books() == []

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
