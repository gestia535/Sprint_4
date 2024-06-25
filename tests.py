import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_existing_book_failed(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'book_name',
        ['', '41 символ в названии книги негативная про',
         '42 символа в названии книги негативная про', '50 символов в названии книги негативная проверка!!']
    )
    def test_add_new_book_add_book_with_length_out_of_range_failed(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_existing_book_success(self, collector):
        collector.add_new_book('Гарри Поттер и Дары смерти')
        collector.set_book_genre('Гарри Поттер и Дары смерти', 'Детективы')
        assert collector.books_genre.get('Гарри Поттер и Дары смерти') == 'Детективы'

    def test_set_book_genre_non_existing_book_failed(self, collector):
        collector.set_book_genre('Гарри Поттер и Дары смерти', 'Детективы')
        assert collector.books_genre.get('Гарри Поттер и Дары смерти') is None

    def test_set_book_genre_non_existing_genre_failed(self, collector):
        collector.add_new_book('Alice in Wonderland')
        collector.set_book_genre('Alice in Wonderland', 'Детская литература')
        assert collector.books_genre.get('Alice in Wonderland') == ''

    def test_get_book_genre_existing_book_success(self, collector):
        collector.add_new_book('Ешь, молись, люби')
        collector.set_book_genre('Ешь, молись, люби', 'Комедии')
        assert collector.get_book_genre('Ешь, молись, люби') == 'Комедии'

    def test_get_book_genre_non_existing_book_failed(self, collector):
        assert collector.get_book_genre('Алые паруса') is None

    def test_get_books_with_specific_genre_get_three_fantastic_success(self, collector):
        collector.books_genre = {'Alice in Wonderland': 'Фантастика', 'Оно': 'Ужасы', 'Шерлок Холмс': 'Детективы',
                                'Красная шапочка': 'Фантастика', 'Незнайка на Луне': 'Фантастика'}
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 3

    def test_get_books_genre_with_book_name_and_genre_success(self, collector):
        collector.add_new_book('Гарри Поттер и Дары смерти')
        collector.set_book_genre('Гарри Поттер и Дары смерти', 'Фантастика')
        assert collector.get_books_genre() == {'Гарри Поттер и Дары смерти': 'Фантастика'}

    def test_get_books_genre_without_books_success(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_genre_without_book_genre_success(self, collector):
        collector.add_new_book('Гарри Поттер и Дары смерти')
        assert collector.get_books_genre() == {'Гарри Поттер и Дары смерти': ''}

    def test_get_books_for_children_get_three_books_success(self, collector):
        collector.books_genre = {'Alice in Wonderland': 'Фантастика', 'Красная шапочка': 'Мультфильмы',
                              'Незнайка на Луне': 'Фантастика', 'Гарри Поттер и Дары смерти': 'Ужасы'}
        assert len(collector.get_books_for_children()) == 3

    def test_get_books_for_children_with_age_rating_only_failed(self, collector):
        collector.books_genre = {'Оно': 'Ужасы', 'Шерлок Холмс': 'Детективы',
                                 'Незнайка на Луне': 'Ужасы', 'Гарри Поттер и Дары смерти': 'Ужасы'}
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_add_one_book_success(self, collector):
        collector.add_new_book('Ешь, молись, люби')
        collector.add_new_book('Малыш и Карлсон')
        collector.add_book_in_favorites('Ешь, молись, люби')
        assert 'Ешь, молись, люби' in collector.favorites

    def test_add_book_in_favorites_add_already_added_failed(self, collector):
        collector.add_new_book('Ешь, молись, люби')
        collector.add_book_in_favorites('Ешь, молись, люби')
        collector.add_new_book('Малыш и Карлсон')
        collector.add_book_in_favorites('Ешь, молись, люби')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_existent_book_success(self, collector):
        collector.add_new_book('Ешь, молись, люби')
        collector.add_new_book('Малыш и Карлсон')
        collector.add_book_in_favorites('Ешь, молись, люби')
        collector.delete_book_from_favorites('Ешь, молись, люби')
        assert 'Ешь, молись, люби' not in collector.favorites

    def test_get_list_of_favorites_books_two_books_in_list_success(self, collector):
        collector.add_new_book('Ешь, молись, люби')
        collector.add_new_book('Малыш и Карлсон')
        collector.add_book_in_favorites('Ешь, молись, люби')
        collector.add_book_in_favorites('Малыш и Карлсон')
        assert collector.get_list_of_favorites_books() == ['Ешь, молись, люби', 'Малыш и Карлсон']