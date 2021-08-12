filename = 'random.txt'

# This will save the string random_text to a file named random.txt
# 'w' means write, you have to explicitly tell the OS that you want to write to file when opening it
# else, f.write won't work.
# with open(filename, 'w', encoding='utf8') as f:  # This was run
# 	f.write(random_text)  # This caused the error, but the previous line created the file with empty content.
# 	f.write(random_text)


# Reading text from file
# with open(filename, 'r', encoding='utf8') as f:
# 	s = f.read()
# print(s)