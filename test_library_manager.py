import datetime
import pytest
from library_manager import add_book, borrow_book, return_book, renew_book, donate_book, search_books, list_available_books, save_books, load_books, save_donations, load_donations

def test_add_book():
    books = {}
    books = add_book("Test Book", "Test Author", "Test Genre", 2021, books)
    assert len(books) == 1
    assert books[1]['title'] == "Test Book"
    assert books[1]['author'] == "Test Author"
    assert books[1]['genre'] == "Test Genre"
    assert books[1]['year'] == 2021
    assert books[1]['available'] == True

def test_borrow_book():
    books = {1: {'title': "Test Book", 'author': "Test Author", 'genre': "Test Genre", 'year': 2021, 'available': True}}
    borrowed_books = {}
    assert borrow_book(1, 30, books, borrowed_books)
    assert not books[1]['available']
    assert borrowed_books[1]['due_date'] == datetime.date.today() + datetime.timedelta(days=30)

def test_return_book():
    books = {1: {'title': "Test Book", 'author': "Test Author", 'genre': "Test Genre", 'year': 2021, 'available': False}}
    borrowed_books = {1: {'due_date': datetime.date.today() + datetime.timedelta(days=30)}}
    assert return_book(1, books, borrowed_books)
    assert books[1]['available']
    assert 1 not in borrowed_books

def test_renew_book():
    borrowed_books = {1: {'due_date': datetime.date.today() + datetime.timedelta(days=30)}}
    assert renew_book(1, 15, borrowed_books)
    assert borrowed_books[1]['due_date'] == datetime.date.today() + datetime.timedelta(days=45)

def test_donate_book():
    donations = {}
    donations = donate_book("Test Book", "Test Author", "Test Genre", 2021, donations)
    assert 1 in donations
    assert donations[1]['title'] == "Test Book"
    assert donations[1]['author'] == "Test Author"
    assert donations[1]['genre'] == "Test Genre"
    assert donations[1]['year'] == 2021

def test_search_books():
    books = {
        1: {'title': "Test Book", 'author': "Test Author", 'genre': "Test Genre", 'year': 2021, 'available': True},
        2: {'title': "Another Book", 'author': "Another Author", 'genre': "Another Genre", 'year': 2020, 'available': True}
    }
    result = search_books("Test", books)
    assert 1 in result
    assert 2 not in result

def test_list_available_books():
    books = {
        1: {'title': "Test Book", 'author': "Test Author", 'genre': "Test Genre", 'year': 2021, 'available': True},
        2: {'title': "Another Book", 'author': "Another Author", 'genre': "Another Genre", 'year': 2020, 'available': False}
    }
    result = list_available_books(books)
    assert 1 in result
    assert 2 not in result

def test_save_load_books():
    books = {
        1: {'title': "Test Book", 'author': "Test Author", 'genre': "Test Genre", 'year': 2021, 'available': True}
    }
    filepath = 'test_books.csv'
    save_books(books, filepath)
    loaded_books = load_books(filepath)
    assert loaded_books == books

def test_save_load_donations():
    donations = {
        1: {'title': "Test Book", 'author': "Test Author", 'genre': "Test Genre", 'year': 2021}
    }
    filepath = 'test_donations.csv'
    save_donations(donations, filepath)
    loaded_donations = load_donations(filepath)
    assert loaded_donations == donations
