from book import Book
from database import Database


# Global variables.

# database should be initialized by init_database()
database = None  # Here we just defined the variable, but it should be initialized in init_database()

# End of global variables


def init_database():
	global database  # Ignore this. This line is needed to overwrite the value of a global variable from a function.
	# TODO: Initialize database (which is a global variable defined at the top of the file).
	
	database = Database()


def show_main_menu():
	
	print('''***********************
*   Library Manager   *
***********************
1. add book
2. remove book
3. search book by name
4. search book by author
5. search book by genre
6. exit''')


def prompt_book():
	# TODO: Ask user to input name, author, genre of a book
	book_name = input('what is the name of the book?')  # NOTE: Python convention is snake_case for variable names, not camelCase
	book_author = input('what is the author of the book?')
	book_genre = input('what genre is this book?')
	book_id = database.get_num_books()
	book = Book(book_name, book_author, book_genre, book_id)
	# This should return a Book object constructed using the information
	# that the user inputted.
	return book


def prompt_user_cmd():
	
	x = input()
	if x == '1':
		# Prompt a book from user and add to database.
		print("add book")
		book = prompt_book()
		database.add_book(book)
		print(database.get_num_books())
	elif x == '2':
		print('''do you want to remove a book?
1: yes
2: no''')
		y = input()
		if y == '1': 
			pass
		elif y == '2':
			pass
		else: 
			print('Unknown choice, click enter to return to main menu')
			ajfewnajf = input("")

		# TODO: Get book information from user, and remove it from database.
	elif x == '3':
		print('What is the name of the book you are searching for?')
		book_name = input()
		result = []
		for book in database.books:
			if book_name == book.name:
				result.append(book)
		if len(result) == 0:
			print("Book not found")
		else:
			i = 0
			print('Books found:')
			while(i < len(result)):
				print('ID ' + str(result[i]._id))
				i = i + 1
				
			
	elif x == '4':
		print('Please type the name of the author')
		book_author = input()
		result = []
		for book in database.books:
			if book_author == book.author:
				result.append(book)
		if len(result) == 0:
			print('Book not found')
		else:
			i = 0
			print('Books found:')
			while(i < len(result)):
				print('ID ' + str(result[i]._id))
				i = i + 1
				
	elif x == '5':
		print('Please type the name of the genre')
		book_genre = input()
		result = []
		for book in database.books:
			if book_genre == book.genre:
				result.append(book)
		if len(result) == 0:
			print('Book not found')
		else:
			i = 0
			print('Books found:')
			while(i < len(result)):
				print('ID ' + str(result[i]._id))
				i = i + 1
	elif x == '6':
		print('exit')
	else:
		raise ValueError("Invalid input, expected 1~6.")  # Just ignore this, this will terminate the program.
	
	
	# Should support adding and removing books
	# syntax: input() will get a string from terminal 
	
	# if input is 1, prompt a book, and add it to database
	# if input is 2, prompt a book, and remove it from database if it exist in it.
	# if input is 3, search all books by name
	# if input is 4, search all books by author
	# if input is 5, search all books by genre

	pass  # TODO: Remove this after implementing this function.

	pass  # TODO: Remove this after implementing this function.


# This will be run in the beginning of everything when executing "python main.py".
def main():
	init_database()
	while(True):
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