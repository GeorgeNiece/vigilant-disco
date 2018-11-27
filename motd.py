motdFile = open('motd.txt')
message = motdFile.read()
print('if you have anything to add to the Message of the Day, type that now')
typedMessage = input()
if typedMessage == '':
	print(message)
else:
	print('\n***********Message of the Day *********************\n')
	print(message)
	print(typedMessage)