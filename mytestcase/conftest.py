'pytest库conftest文件：存放勾子函数，用于在测试用例执行前、中、后时自动调用该文件下的函数'
'可以将测试固件（fixture）定义到该文件下'
''
import pytest

@pytest.fixture(scope='function')
def aa():
	pass

