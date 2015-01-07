try:
	data = open('sketch.txt')

	try:
		for each_line in data:
			if not each_line.find(':') == -1:
				(role, line_spoken) = each_line.split(':', 1)
				print(role, end='')
				print(' said: ', end='')
				print(line_spoken, end='')

	except ValueError as verr:
		print("Oops, an error occurred: ", verr)

except IOError as err:
	print("Oops, the data file is missing: ", err)

finally:
	data.close()