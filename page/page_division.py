'被测功能的项目文件'
'相当于PO设计模式中页面对象层的封装'


class NumberDivision(object):
	"""docstring for number"""
	def __init__(self):
		#self.divisionnum = None
		pass

	def division_num(self,a ,b):
		if b is 0:
			return 'Divisor can not be zero'
		else:
			return int(a / b)




