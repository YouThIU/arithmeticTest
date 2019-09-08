	
from subline_pytest.page.page_division import NumberDivision
import pytest

@pytest.fixture(scope='function')
def number(request):
	print('setup每个用例执行：开始执行')
	number = NumberDivision()
	def teardown():
		print('teardown每个用例执行：结束执行')
	request.addfinalizer(teardown)
	return number


@pytest.fixture(scope='module')
def module():
	print('setup每个模块执行：开始执行')
	yield
	print('teardown每个模块执行：结束执行')


@pytest.fixture()
def cmdopt(request):
	# 得到命令行参数的值
	return request.config.getoption('--cmdopt')


@pytest.fixture(scope='package',autouse=True)
def auto_package():
	print('autouse为True，package执行一次；开始执行')
	yield
	print('autouse为True，package执行一次；结束执行')