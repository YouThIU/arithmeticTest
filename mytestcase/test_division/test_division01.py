'类式编写测试用例'
import pytest

'''xfail标记的使用的基本思路是将01作为前置条件，02和03调用01，
、在执行02和03时判断01的状态，如果失败，则用例标记为xfail。成功，则执行下面语句'''

'----------练习xfail标记的使用场景'
@pytest.fixture(scope='function')
def mydivision():
	pwd = 1
	if pwd:
		name = 1
	else:
		name = 0
	return name


def test_division_02(number,mydivision):
	'''测试用例01'''
	#mydivision = 0
	# print(mydivision)
	if mydivision:
		data = number.division_num(2,2)
		assert data is 1
	else:
		# 失败就跳过当前用例，执行下面的用例
		pytest.xfail('用例跳过，标记为xfail')


def test_division_03(number,mydivision):
	'''pytest.xfail在用例内部跳过用例的测试用例'''
	#mydivision = 1
	#print(mydivision)
	if mydivision:
		data = number.division_num(2,2)
		assert data is 1
	else:
		pytest.xfail('用例跳过，标记为xfail')


'----------fixture传参request的使用'
ids=['第一个','第二个','第三个']
@pytest.fixture(scope='function')
def mydivision01(request):
	mylist = []
	#通过request.param拿到参数赋值给myparam
	myparam = request.param
	print(f'当前参数是{myparam}')
	mylist.append(myparam)
	return mylist

data1 = [(1,1),(2,2),(3,3)]
data2 = [1,2,3]
@pytest.mark.parametrize('mydivision01',data1,ids=ids,indirect=True)
def test_division_04(mydivision01,number):
	"""fixture传入request参数来获取用例数据的测试用例"""
	# print(mydivision01)
	if len(mydivision01[0]) is 1:	
		pytest.xfail('参数不足，用例跳过')
	else:
		data = number.division_num(mydivision01[0][0], mydivision01[0][1])
		assert data is 1

def test_division_05(number, cmdopt):
	"""命令行参数的使用的测试用例"""
	if cmdopt == 'type1':
		print('执行了命令type1')
		data = number.division_num(6,2)
		assert data is 3
	elif cmdopt == 'type2':
		print('执行了命令type2')
		data = number.division_num(2,6)
		assert data is 0
	else:
		raise NameError('my option:type1 or type2')

