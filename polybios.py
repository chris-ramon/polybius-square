			#  0	1	  2	   3	4	  5    
row0 		= ["",  "A", "B", "C", "D", "E"];
row1 		= ["A", "A", "B", "C", "D", "E"];
row2 		= ["B", "F", "G", "H", "IJ", "K"];
row3 		= ["C", "L", "M", "N", "O", "P"];
row4 		= ["D", "Q", "R", "S", "T", "U"];
row5 		= ["E", "V", "W", "X", "Y", "Z"];

num0 		= ["",  "1", "2", "3", "4", "5"];
num1 		= ["1", "A", "B", "C", "D", "E"];
num2 		= ["2", "F", "G", "H", "IJ", "K"];
num3 		= ["3", "L", "M", "N", "O", "P"];
num4 		= ["4", "Q", "R", "S", "T", "U"];
num5 		= ["5", "V", "W", "X", "Y", "Z"];

matrix_letters  = [row0, row1, row2, row3, row4, row5] 
matrix_numbers  = [num0, num1, num2, num3, num4, num5] 

def polybios_cypher(plain_text, which_matrix):
	matrix = matrix_letters if which_matrix == "letter" else matrix_numbers
	c1 = []
	for letter in plain_text.replace(" ",""):
		row = 1
		while row < len(matrix):
			col = 1
			while col < len(row1):
				if letter.upper() == matrix[row][col] or \
					letter.upper() == matrix[row][col][:1] or \
					letter.upper() == matrix[row][col][:2]:

					c1.append(matrix[row][0]+matrix[0][col])
				col = col + 1
			row = row + 1
	return " ".join(c1)

def polybios_decypher(cyphered_text, which_matrix):
	matrix = matrix_letters if which_matrix == "letter" else matrix_numbers
	CYPHERED_TEXT = cyphered_text.replace(" ","")
	_range = 0
	GROUPS = len(CYPHERED_TEXT) / 2
	DECYPHERED = []
	for j in range(0,GROUPS):
		letters = CYPHERED_TEXT[_range:_range+2]
		_range += 2
		for letter in letters:
			col = 0
			row = 0
			while row < len(matrix_letters):
				if matrix[row][col] == letter:
					i = row
					DECYPHERED.append(i)
					break
				row += 1
	plain_text = ''
	_range = 0
	for i in range(0, len(DECYPHERED)/2 ):
		plain_text += matrix[DECYPHERED[_range]][DECYPHERED[_range+1]]
		_range += 2

	return plain_text












