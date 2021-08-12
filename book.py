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
		

	def to_str(self):
		'''Return a string containing info of this book'''
		return str(self._id) + '\t' + self.name + '\t' + self.author + '\t' + self.genre
		
	def from_str(self, s):
		'''
		Extract info from a string, and assign the values to self. 
		string format: <id>\t<name>\t<author>\t<genre>
		'''
		
		# TODO: Create a book instance from string
		# tips: 
		# self._id = ....
