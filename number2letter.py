# Just something that gets numbers from the user and converts it into letters.
# Probably made this for turtler's escape room.

reference = [x for x in 'abcdefghijklmnopqrstuvwxyz'] 

def small_convertor(num):
	# converts number into letter
	num = num - 1 # to start counting from 0
	moduled = (num % 26) 
	return reference[moduled]

if __name__ == '__main__':
	current = ''

	first_num = 0
	while first_num != -3:
		# keeps getting input from user
		# if the received is -3, it ends
		# if it is -2, it resets the sentence
		# if it is -1, it moves into another word (space)

		print(current)
		first_num = input('number: ')

		try:
			first_num = int(first_num)
		except:
			continue	



		if first_num == -1:
			current += ' '
			continue

		elif first_num == -2:
			current = ''
			continue	

		elif first_num < -2:
			continue	

		current += small_convertor(first_num)
