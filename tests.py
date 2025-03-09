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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # Тест на проверку добавления жанра книге
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', 'Фантастика')

        assert collector.get_book_genre('Тестовая книга') == 'Фантастика'

    #Тест на проверку, что жанр книги добавляется корректно
    def test_set_book_genre_non_existent_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', 'Научная фантастика')

        assert collector.get_book_genre('Тестовая книга') == ''

    #Тест на проверку, что жанр книги возвращается корректно
    @pytest.mark.parametrize(
        'name_book, book_genre',
        [
            ['Оно', 'Ужасы'],
            ['Властелин колец', 'Фантастика'],
            ['Игра ангела', 'Комедии']
        ]
    )
    def test_get_book_genre(self, name_book, book_genre):
        collector = BooksCollector()

        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, book_genre)

        assert collector.get_book_genre(name_book) == book_genre

    #Тест на проверку, что возвращаются книги с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Властелин колец','Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер','Властелин колец']

    #Тест на проверку получения словаря books_genre
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула','Ужасы')

        assert collector.get_books_genre() == {'Дракула': 'Ужасы'}

    #Тест на проверку возврата книг, которые подходят детям
    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Малыш и Карлсон, который живёт на крыше')
        collector.add_new_book('Оно')
        collector.set_book_genre('Малыш и Карлсон, который живёт на крыше', 'Фантастика')
        collector.set_book_genre('Оно','Ужасы')

        assert collector.get_books_for_children() == ['Малыш и Карлсон, который живёт на крыше']

    #Тест на добавление книги в Избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')

        assert 'Властелин колец' in collector.get_list_of_favorites_books()

    #Тест на удаление книги из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')

        assert 'Дюна' not in collector.get_list_of_favorites_books()

    #Тест на выдачу списка книг в Избранном
    def test_get_list_of_favorites_book(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_new_book('Академия')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Академия')

        assert collector.get_list_of_favorites_books() == ['Властелин колец','Академия']