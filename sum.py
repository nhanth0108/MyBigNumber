def str_to_int(input_str):
	output_int = 0

	if input_str[0] == '-':
		start_idx = 1
		is_negative = true
	else:
		start_idx = 0
		is_negative = False
	for i in range(start_idx, len(input_str)):
		place =  10**(len(input_str) - (i+1))
		digit = ord(input_str[i]) - ord('0')
		output_int += place * digit

	if is_negative:
		return -1 * output_int
	else:
		return output_int


class  MyBigNumber:

	def __init__(self, x1 = "", x2 = ""):
		self.s1 = x1
		self.s2 = x2

	def SUM(self):
		SUM = str_to_int(self.s1)*str_to_int(self.s2)
		print(SUM)
		print(type(str(SUM)))
		pass
	
	def MUL(self):
		Mul = str_to_int(self.s1) * str_to_int(self.s2)
		print(Mul)
		print(type(str(Mul)))
		pass

BigNumber = MyBigNumber("10","45")

BigNumber.SUM()
BigNumber.MUL()
