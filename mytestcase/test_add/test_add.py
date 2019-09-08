'函数式编写测试用例'
'练习pytest中的skip'
import pytest
import os
from page import page_add


# 若想跳过整个模块的测试用例，使用pytest.mark.skip或pytest.mark.skipif的方法。
# 注意：整个模块所有测试用例跳过时需要全局的pytestmark作为变量。这种方法作用于整个模块，故不用使用@的方法给测试用例添加装饰器，只需要在模块顶部写成这样后，会自动判断条件是否为真或假
# 可以跨模块调用skip或skipif标记（只需要在别的模块引入即可）
#pytestmark = pytest.mark.skip('跳过整个模块的测试用例', allow_module_level=True)
#pytestmark = pytest.mark.skipif(2>1,reason='跳过整个模块的测试用例')

# 单个测试用例使用skipif跳过测试用例也可以预先定义好（与在测试用例上加装饰器的效果一样），但是变量名不能是pytestmark,这个变量名是作用于整个模块的用例
wangyuanchao = pytest.mark.skipif(2>1,reason='跳过整个模块的测试用例')


@wangyuanchao
def test_add_01(number):
	"""数字算法：两个正整数相加"""
	data = number.add_num(1, 2)
	assert data is 3

@pytest.mark.skip('跳过单个测试用例')
def test_add_02(number, module):
	# 在测试执行或设置期间跳过测试用例,等同于pytest.mark.skip()
	# pytest.skip('跳过单个用例')
	data = number.add_num(0,0)
	assert data is 0

'''def test_add_03(mprint):
	"""测试用例异常时，依旧会执行teardwon操作，与unittest一样"""
	data = mprint.add_num('da', 'da')
	assert data is 0'''

@pytest.mark.skipif(2>1, reason='条件为真，跳过单个测试用例')
def test_add_04(mprint):
	data = mprint.add_num(2,2)
	assert data is 4


"""pytest的参数化装饰器，第一个参数是参数名，用于测试用例的参数。第二个参数是测试数据，由列表组成，若参数是两个及两个以上，则列表由多个元组组成，元组中的每个元素对应每个参数"""
"""第三个参数是标记为失败的用例就不执行了，直接跳过显示为xpasseed"""
@pytest.mark.parametrize('num, expect', [([1,2], 3), ([2,2], 4), ([3,3], 6),
						pytest.param([4,4], 8, marks=pytest.mark.xfail)])
def test_add_05(number, num, expect):
	data = number.add_num(num[0], num[1])
	assert data is expect

"""多个参数化参数的组合情况，可以叠代参数化装饰器，其组合后的参数顺序是1.1、2.1、1.2、2.2"""
@pytest.mark.parametrize('num1', [1,2])
@pytest.mark.parametrize('num2', [1,2])
#@pytest.mark.parametrize('expect', [2,3,3,4])
def test_add_06(number, num1, num2):
	data = number.add_num(num1, num2)
	assert data in {2,3,4}

'''def test_add_07():
	"""断言异常"""
	# raise
	with pytest.raises(ZeroDivisionError) as zde:
		1/0

	# print(zde.type)
	# print(str(zde.value))
	# 断言异常的类型
	assert zde.type == ZeroDivisionError
	# 断言异常的value值
	assert str(zde.value) in 'division by zero'
	'''

def test_add_07(number):
	# 导入模块（库，py文件，类，方法，变量）失败,则跳过测试用例，成功则执行单个测试用例
	# 作用于测试用例里面。书上说可以跳过整个模块的测试用例，不知道咋实现
	pytest.importorskip('dada')
	data = number.add_num(1, 1)
	assert data is 2

