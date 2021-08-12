from book import Book

# Now I want to save this to a file
def save_books(filename, books):
	'''
	Save a list of Books to a file.
	Parameters:
		filename: str,
		books: list of Books,
	'''
	with open(filename, 'w', encoding='utf8') as f:
		# Turn each book into a string, then save one string each line
		for b in books:
			s = b.to_str()
			f.write(s + '\n')  	# NOTE: write() doesn't add '\n' by default like print()


def load_books(filename):
	'''
	Load a list of Books from a file where each line represents one Book.
	The file format:
		line 1: <id>\t<name>\t<author>\t<genre>
		line 2: <id>\t<name>\t<author>\t<genre>
		...
	'''
	books = []
	with open(filename, 'r', encoding='utf8') as f:
		for line in f:  # Loop each line
			line = line.strip()  # This remove "whitespaces" (invisible chars such as ' ', '\t', '\n', etc) on leftmost and rightmost end.
			line = line.split('\t')  # This returns a list containing strings that are separated by '\t' (TAB).
			# Eg: 'Donny Chan\t22\t1234' -> ['Donny Chan', '22', '1234']
			# So now: line = ['Example Name', 'example age']
			_id = int(line[0])
			name = line[1]
			author = line[2]
			genre = line[3]


			books.append(Book(name, author, genre, _id))
	return books