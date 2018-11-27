# Script to echo our message of the day and insert an additional message if desired

motdFile = open('motd.txt') # our motd file is in the same folder as the code
message = motdFile.read()
print('if you have anything to add to the Message of the Day, type that now')
typedMessage = input()
if typedMessage == '':
	print(message)
else:
	# Here we want to put in a multi-line
	# comment and note that we want to indent to match the code
	print('\n***********Message of the Day *********************\n')
	print(message)
	print(typedMessage)