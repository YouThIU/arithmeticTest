'函数式编写测试用例'
'练习pytest中的自定义mark'
import pytest
from selenium import webdriver

# pytest -v -m not division01:不执行标记了division01的测试用例
@pytest.mark.division01
def test_division_01(number):
	"""自定义mark，作用是只执行带有division01的测试用例，命令行使用pytest -v -m division01"""
	data = number.division_num(2,1)
	assert data is 2


# pytest.main(['-v','-m=not division02'])
@pytest.mark.division02
def test_division_02(number):
	"""自定义mark，作用是只执行带有division01的测试用例，程序内使用pytest.main(['-v','-m=division02'])"""
	data = number.division_num(2,2)
	assert data is 1

# 普通测试用例
def test_division_03(number):
	data = number.division_num(0,1)
	assert data is 0



#def test_division_04(browser):
	#assert browser.title == 'dada'
