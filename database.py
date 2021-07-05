# Holds a class for database.

class Database:
	# TODO: add methods
	def __init__(self): 
		# TODO: implement
		self.books = []

	def get_num_books(self):
		# len(array) gives the size of the array
		return len(self.books)

	def add_book(self, book):
		self.books.append(book)
	
	def remove_book(self, book_id):
		for book in self.books:
			if book._id == book_id:
				self.books.remove(book) 

    # def find_book_by_author(self, query):
    #   ...

	# def find_book_by_name(self, ...)

	# def find_book_by_genre...

	# def is_available
