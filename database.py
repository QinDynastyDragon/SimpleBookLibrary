# Holds a class for database.

class Database:
	def __init__(self):
		self.books = []
		self.id_counter = 0

	def get_new_bookID(self):
		# len(array) gives the size of the array
		return self.id_counter

	def add_book(self, book):
		self.books.append(book)
		self.id_counter += 1
	
	def remove_book(self, book_id):
		''' Remove a book by ID '''
		for book in self.books:
			if book._id == book_id:
				self.books.remove(book) 

	def find_book_by_author(self, query):
		res = []
		for book in self.books:
			if book.author == query:
				res.append(book)
		return res

	def find_book_by_name(self, query):
		res = []
		for book in self.books:
			if book.name == query:
				res.append(book)
		return res

	def find_book_by_genre(self, query):
		res = []
		for book in self.books:
			if book.genre == query:
				res.append(book)
		return res
