'pytest库conftest文件：存放勾子函数，用于在测试用例执行前、中、后时自动调用该文件下的函数'
'可以将测试固件（fixture）定义到该文件下'
'该'
import pytest
from page.page_add import NumberAdd


@pytest.fixture(scope='function')
def number():
	"""哪个测试用例需要调用函数级别的fixture，那就将fixture名作为测试用例的参数"""
	number = NumberAdd()
	return number

@pytest.fixture(scope='function')
def mprint(number, request):
	print('setup_function每个函数执行一次：开始执行测试用例')
	def teardown():
		print('teardown_function每个函数执行一次：结束执行测试用例')

	request.addfinalizer(teardown)
	return number

'''@pytest.fixture(scope='function')
def mprint01(number, request):
	# print('setup_function每个函数执行一次：开始执行测试用例')
	assert NameError
	yield
	print('teardown_function每个函数执行一次：结束执行测试用例')
	return number'''

@pytest.fixture(scope='module')
def module(request):
	"""哪个测试用例需要调用模块级别的fixture，那就将fixture名作为测试用例的参数"""
	i = 1
	print('setup_module每个模块执行一次：开始执行测试用例')
	def teardown():
		print(f'teardown_module每个模块执行一次：结束执行测试用例{i}')

	request.addfinalizer(teardown)

