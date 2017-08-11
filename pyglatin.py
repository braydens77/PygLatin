def get_input():
	# Obtain the user's input
	input = raw_input("Enter some words: ")
	return input

def translate(input):
	# Check if user input is empty
	if len(input) > 0:
		words = input.split()
		
		# Ensure words contain only alphabetical characters
		is_acceptable = True
		for word in words:			
			if not word.isalpha():
				is_acceptable = False
				
		# If input is ok, translate all of the words
		if is_acceptable:
			translated_words = []
			pyg = "ay"
			for word in words:
				new_word= word.lower()
				first = new_word[0]
				new_word = word + first + pyg
				new_word = new_word[1:len(new_word)]
				translated_words.append(new_word)
			
			# Print the translation
			for new_word in translated_words:
				print new_word,
			print "\n"
			
			# Restart
			translate(get_input())
			
		# Input is not ok. Print error message
		else:
			print "Sorry, please use only alphabetical characters!\n"
			translate(get_input())
			
	else:
		# Input was empty. Print an error
		print "Sorry, please enter a word or sentence."
		translate(get_input())

		
# Start of program
print "Welcome to PygLatin!"
translate(get_input())