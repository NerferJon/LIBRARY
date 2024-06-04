import datetime
import csv

# Lista inicial de livros
books = {
    1: {'title': "Harry Potter and the Philosopher's Stone", 'author': "J.K. Rowling", 'genre': "Fantasy", 'year': 1997, 'available': True},
    2: {'title': "Harry Potter and the Chamber of Secrets", 'author': "J.K. Rowling", 'genre': "Fantasy", 'year': 1998, 'available': True},
    3: {'title': "Harry Potter and the Prisoner of Azkaban", 'author': "J.K. Rowling", 'genre': "Fantasy", 'year': 1999, 'available': True},
    4: {'title': "Harry Potter and the Goblet of Fire", 'author': "J.K. Rowling", 'genre': "Fantasy", 'year': 2000, 'available': True},
    5: {'title': "Harry Potter and the Order of the Phoenix", 'author': "J.K. Rowling", 'genre': "Fantasy", 'year': 2003, 'available': True},
    6: {'title': "Harry Potter and the Half-Blood Prince", 'author': "J.K. Rowling", 'genre': "Fantasy", 'year': 2005, 'available': True},
    7: {'title': "Harry Potter and the Deathly Hallows", 'author': "J.K. Rowling", 'genre': "Fantasy", 'year': 2007, 'available': True},
    8: {'title': "The Lord of the Rings: The Fellowship of the Ring", 'author': "J.R.R. Tolkien", 'genre': "Fantasy", 'year': 1954, 'available': True},
    9: {'title': "The Lord of the Rings: The Two Towers", 'author': "J.R.R. Tolkien", 'genre': "Fantasy", 'year': 1954, 'available': True},
    10: {'title': "The Lord of the Rings: The Return of the King", 'author': "J.R.R. Tolkien", 'genre': "Fantasy", 'year': 1955, 'available': True},
    11: {'title': "The Catcher in the Rye", 'author': "J.D. Salinger", 'genre': "Fiction", 'year': 1951, 'available': True},
    12: {'title': "The Bible", 'author': "Various", 'genre': "Religious", 'year': 0, 'available': True},
    13: {'title': "The Book of Mormon", 'author': "Various", 'genre': "Religious", 'year': 1830, 'available': True},
    14: {'title': "1984", 'author': "George Orwell", 'genre': "Dystopian", 'year': 1949, 'available': True},
    15: {'title': "Animal Farm", 'author': "George Orwell", 'genre': "Satire", 'year': 1945, 'available': True},
    16: {'title': "The Hobbit", 'author': "J.R.R. Tolkien", 'genre': "Fantasy", 'year': 1937, 'available': True},
    17: {'title': "Iliad", 'author': "Homer", 'genre': "Epic", 'year': -750, 'available': True},
    18: {'title': "The Odyssey", 'author': "Homer", 'genre': "Epic", 'year': -700, 'available': True},
    19: {'title': "Crime and Punishment", 'author': "Fyodor Dostoevsky", 'genre': "Philosophical", 'year': 1866, 'available': True},
    20: {'title': "War and Peace", 'author': "Leo Tolstoy", 'genre': "Historical", 'year': 1869, 'available': True},
    21: {'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'genre': "Fiction", 'year': 1960, 'available': True},
    22: {'title': "Pride and Prejudice", 'author': "Jane Austen", 'genre': "Romance", 'year': 1813, 'available': True},
    23: {'title': "Moby Dick", 'author': "Herman Melville", 'genre': "Adventure", 'year': 1851, 'available': True},
    24: {'title': "The Great Gatsby", 'author': "F. Scott Fitzgerald", 'genre': "Fiction", 'year': 1925, 'available': True},
    25: {'title': "Little Women", 'author': "Louisa May Alcott", 'genre': "Fiction", 'year': 1868, 'available': True}
}

borrowed_books = {}
donations = {}

def add_book(title, author, genre, year, books):
    book_id = len(books) + 1
    books[book_id] = {'title': title, 'author': author, 'genre': genre, 'year': year, 'available': True}
    return books

def borrow_book(book_id, days, books, borrowed_books):
    if book_id in books and books[book_id]['available']:
        due_date = datetime.date.today() + datetime.timedelta(days=days)
        books[book_id]['available'] = False
        borrowed_books[book_id] = {'due_date': due_date}
        return True
    return False

def return_book(book_id, books, borrowed_books):
    if book_id in books and not books[book_id]['available']:
        books[book_id]['available'] = True
        borrowed_books.pop(book_id, None)
        return True
    return False

def renew_book(book_id, additional_days, borrowed_books):
    if book_id in borrowed_books:
        borrowed_books[book_id]['due_date'] += datetime.timedelta(days=additional_days)
        return True
    return False

def donate_book(title, author, genre, year, donations):
    donation_id = len(donations) + 1
    donations[donation_id] = {'title': title, 'author': author, 'genre': genre, 'year': year}
    return donations

def search_books(keyword, books):
    return {book_id: details for book_id, details in books.items() if 
            keyword.lower() in details['title'].lower() or 
            keyword.lower() in details['author'].lower() or 
            keyword.lower() in details['genre'].lower() or 
            keyword in str(details['year'])}

def list_available_books(books):
    return {book_id: details for book_id, details in books.items() if details['available']}

def save_books(books, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for book_id, details in books.items():
            writer.writerow([book_id, details['title'], details['author'], details['genre'], details['year'], details['available']])

def load_books(filename):
    books = {}
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                book_id, title, author, genre, year, available = row
                books[int(book_id)] = {'title': title, 'author': author, 'genre': genre, 'year': int(year), 'available': available == 'True'}
    except FileNotFoundError:
        pass
    return books

def save_donations(donations, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for donation_id, details in donations.items():
            writer.writerow([donation_id, details['title'], details['author'], details['genre'], details['year']])

def load_donations(filename):
    donations = {}
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                donation_id, title, author, genre, year = row
                donations[int(donation_id)] = {'title': title, 'author': author, 'genre': genre, 'year': int(year)}
    except FileNotFoundError:
        pass
    return donations

# Main loop
if __name__ == "__main__":
    while True:
        print("\nWelcome to Biblioteca Jonathan!")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Renew Book")
        print("5. Donate Book")
        print("6. Search Books")
        print("7. List Available Books")
        print("8. Save and Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            genre = input("Enter the genre: ")
            year = int(input("Enter the year: "))
            books = add_book(title, author, genre, year, books)
            print(f"Book '{title}' added successfully!")
        
        elif choice == "2":
            book_id = int(input("Enter the book ID to borrow: "))
            days = int(input("Enter the number of days to borrow: "))
            if borrow_book(book_id, days, books, borrowed_books):
                print(f"Book ID {book_id} borrowed successfully!")
            else:
                print("Book not available for borrowing.")
        
        elif choice == "3":
            book_id = int(input("Enter the book ID to return: "))
            if return_book(book_id, books, borrowed_books):
                print(f"Book ID {book_id} returned successfully!")
            else:
                print("Failed to return the book.")
        
        elif choice == "4":
            book_id = int(input("Enter the book ID to renew: "))
            additional_days = int(input("Enter the additional number of days: "))
            if renew_book(book_id, additional_days, borrowed_books):
                print(f"Book ID {book_id} renewed successfully!")
            else:
                print("Failed to renew the book.")
        
        elif choice == "5":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            genre = input("Enter the genre: ")
            year = int(input("Enter the year: "))
            donations = donate_book(title, author, genre, year, donations)
            print(f"Book '{title}' donated successfully!")
        
        elif choice == "6":
            keyword = input("Enter a keyword to search: ")
            results = search_books(keyword, books)
            if results:
                print("Search Results:")
                for book_id, details in results.items():
                    print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Genre: {details['genre']}, Year: {details['year']}, Available: {details['available']}")
            else:
                print("No books found.")
        
        elif choice == "7":
            available_books = list_available_books(books)
            if available_books:
                print("Available Books:")
                for book_id, details in available_books.items():
                    print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Genre: {details['genre']}, Year: {details['year']}")
            else:
                print("No books available.")
        
        elif choice == "8":
            save_books(books, 'books.csv')
            save_donations(donations, 'donations.csv')
            print("Data saved. Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
