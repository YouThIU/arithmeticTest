'函数式编写测试用例'
'fixture参数autouse=True时，用例自动调用'
'注意：class和function在一起时，function会覆盖class'
import pytest

@pytest.fixture(scope='module',autouse=True)
def auto_module():
	print('autouse为True，module执行一次；开始执行')
	yield
	print('autouse为True，module执行一次；结束执行')

@pytest.fixture(scope='class',autouse=True)
def auto_module():
	print('autouse为True，class执行一次；开始执行')
	yield
	print('autouse为True，class执行一次；结束执行')	

@pytest.fixture(scope='function',autouse=True)
def auto_module():
	print('autouse为True，function执行一次；开始执行')
	yield
	print('autouse为True，function执行一次；结束执行')


def test_division_01():
	print('01')


# pytest.main(['-v','-m=not division02'])
def test_division_02(number):
	print('02')

class Test_Login():
	def test_division_03(number):
		print('03')