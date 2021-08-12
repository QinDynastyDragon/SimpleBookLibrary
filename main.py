from book import Book
from database import Database
from save_load import *


# Global variables.
database = None  # Here we just defined the variable, but it should be initialized in init_database()

# End of global variables
def init_database():
	global database  # Ignore this. This line is needed to overwrite the value of a global variable from a function.
	database = Database()


def show_main_menu():
	print('''***********************
*   Library Manager   *
***********************
1. Add book
2. Remove book
3. Search book by name
4. Search book by author
5. Search book by genre
6. Show all books
7. Save
8. Load
9. Reset database
10. Exit''')


def prompt_book():
	# TODO: Ask user to input name, author, genre of a book
	print('Enter the name of the book.')
	book_name = input('>>> ')
	print('Enter the name of the author.')
	book_author = input('>>> ')
	print('Enter the genre of the book.')
	book_genre = input('>>> ')
	book_id = database.get_new_bookID()
	book = Book(book_name, book_author, book_genre, book_id)
	# This should return a Book object constructed using the information
	# that the user inputted.
	return book


def show_books(books):
	'Print a list of books in a formatted way. One book each line.'
	id_header = 'ID'
	name_header = 'Name'
	author_header = 'Author'
	genre_header = 'Genre'
	print('')
	print(f'{id_header:>6}: {name_header:<32} {author_header:<24} {genre_header:<16}')
	print('-' * 84)
	for book in books:
		print(f'{book._id:>6}: {book.name:<32} {book.author:<24} {book.genre:<16}')
	print('-' * 84)
	print('')

def get_book_by_name():
	print('Enter name.')
	name = input('>>> ')
	return database.find_book_by_name(name)

def get_book_by_author():
	print('Enter author.')
	author = input('>>> ')
	return database.find_book_by_author(author)

def get_book_by_genre():
	print('Enter genre.')
	genre = input('>>> ')
	return database.find_book_by_author(genre)

def handle_search(cmd):
	'''Handle searching. Prompt query and print matching books.'''
	assert cmd in ['3', '4', '5']
	result = None
	if cmd == '3':
		result = get_book_by_name()
	elif cmd == '4': 
		result = get_book_by_author()
	else:
		result = get_book_by_genre()

	if len(result) == 0:
		print("< No matching books not found >\n")
	else:
		show_books(result)


def prompt_user_cmd():
	cmd = input('>>> ')
	if cmd == '1':
		# Prompt a book from user and add to database.
		book = prompt_book()
		database.add_book(book)
		print("Book with ID " + str(book._id) + " added to database.")
		# print("Book with ID",book._id,"added to database.")
		# print(f"Book with ID {book._id} added to database.")
		print(f'Total number of books: {database.get_new_bookID()}')
	elif cmd == '2':
		print('Do you want to remove a book?\n'
			  '1: Yes\n'
			  '2: No')
		remove = input('>>> ')
		if remove == '1': 
			print('''1: Remove book by ID.
2: Remove book by name.
3: Remove book by author.
4: Remove book by genre. >''')
			remove_by = int(input('>>> ')) 
			if remove_by == 1:
				pass
			elif remove_by == 2:
				books_to_delete = get_book_by_name()
				show_books(books_to_delete)
				print('Enter the ID of the book to be deleted\n')
				bookID_to_delete = int(input('>>> '))
				database.remove_book(bookID_to_delete)
				
			elif remove_by == 3:
				books_to_delete = get_book_by_author()
				show_books(books_to_delete)
				print('Enter the ID of the book to be deleted\n')
				bookID_to_delete = int(input('>>> '))
				database.remove_book(bookID_to_delete)
			elif remove_by == 4:
				books_to_delete = get_book_by_genre()
				show_books(books_to_delete)
				print('Enter the ID of the book to be deleted\n')
				bookID_to_delete = int(input('>>> '))
				database.remove_book(bookID_to_delete)
		elif remove == '2':
			pass 
		else: 
			print('< Unknown choice, click enter to return to main menu. >\n')

		# TODO: Get book information from user, and remove it from database.
	elif cmd == '3' or cmd == '4' or cmd == '5':
		handle_search(cmd)
	elif cmd == '6':
		show_books(database.books)
		pass
	elif cmd == '7': # Save file
		print('Save the library in a text file?\n'
			  '1: Yes\n'
			  '2: No')
		savefile = input('>>> ')
		if savefile == '1':
			save_books('list_of_books.txt', database.books)
		elif savefile == '2':
			pass
		else:
			print('< Unknown choice, click enter to return to main menu. >\n')
	elif cmd == '8': # Load file, print in the terminal
		print('Load and show the books from the saved files?\n'
			  '1: Yes\n'
			  '2: No')
		loadfile = input('>>> ')
		if loadfile == '1':
			loadbooks = load_books('list_of_books.txt')
			database.id_counter = 0
			database.books = []
			for book in loadbooks:
				database.add_book(book)
		elif loadfile == '2':
			pass
		else:
			print('< Unknown choice, click enter to return to main menu. >\n')

		pass
	elif cmd == '9':
		pass
	elif cmd == '10':
		print('< Exiting application... >')
		exit()


# This will be run in the beginning of everything when executing "python main.py".
def main():
	init_database()
	while True:
		show_main_menu()
		prompt_user_cmd()


# The following is a Python convention.
# __name__ is a built-in keyword, which will be equal to "__main__"
# when you execute 'python main.py' in the terminal ("main.py" is
# the name of this file).

# The reason we use this is to avoid main() from running when importing
# this file from somewhere else, because when being imported, __name__
# does not equal "__main__".
if __name__ == "__main__":
	main()