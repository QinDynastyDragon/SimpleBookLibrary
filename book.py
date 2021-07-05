# This file holds the class of book

class Book:
	'''
	Book class for holding name, author and genre.
	'''
	# TODO: implement this class
	# I think a Book should have the following members:
	# - _id
	# - name
	# - author
	# - genre
	
	def __init__(self, name, author, genre, _id=None):
		self.name = name
		self.author = author
		self.genre = genre
		self._id = _id
		
		# "self" is equivalent to "this" in many other languages, 
		# which is a pointer to an object itself.
		# NOTE: "self" is not passed from outside.
		

	def get_str(self):
		pass
		# TODO: Return a string containing info of this book
		# This is so that we can print list of books to the terminal.