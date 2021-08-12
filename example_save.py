class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

jimmy = Person('Jimmy Chan', 27)
donny = Person('Donny Chan', 22)

persons = [jimmy, donny]
filename = 'persons.txt'

# Now I want to save this to a file
def save_persons(filename, persons):
	'''
	Save a list of Person to a file.
	Parameters:
		filename: str,
		persons: list of Person,
	'''
	with open(filename, 'w', encoding='utf8') as f:
		# Turn each person into a string, then save one string each line
		for p in persons:
			s = p.name + '\t' + str(p.age)  # Turn the member variables into string, use TAB-Separated because names can have spaces.
			f.write(s + '\n')  				# NOTE: write() doesn't add '\n' by default like print()


def load_persons(filename):
	'''
	Load a list of Person from a file where each line represents one Person.
	The file format:
		line 1: <name>\t<age>
		line 2: <name>\t<age>
		...
	'''
	persons = []
	with open(filename, 'r', encoding='utf8') as f:
		for line in f:  # Loop each line
			# Now, line is a string, its value is one line
			# NOTE: How to turn each line into a Person? How do we know which part is name, and which part is age?
			line = line.strip()  # This remove "whitespaces" (invisible chars such as ' ', '\t', '\n', etc) on leftmost and rightmost end.
			line = line.split('\t')  # This returns a list containing strings that are separated by '\t' (TAB).
			# Eg: 'Donny Chan\t22\t1234' -> ['Donny Chan', '22', '1234']
			# So now: line = ['Example Name', 'example age']
			name = line[0]
			age = int(line[1])

			# The following 3 lines are stupid.
			# name = line[:10]  # String consisting of first 10 chars of line.
			# # age = line[:2]    # String consisting of last 2 chars of line.  NOTE: WRONG, because last three chars are "27\n".
			# age = line[-3:-1]  # String consisting of line[-3] and line[-2]. 

			persons.append(Person(name, age))
	return persons
		

save_persons(filename, persons)

# Load persons
persons = load_persons(filename)
for p in persons:
	print(p.name, p.age)
