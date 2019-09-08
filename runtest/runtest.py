import os,sys
curpath = os.path.abspath(os.path.dirname(__file__))
# 获取项目的路径
rootpath = os.path.split(curpath)[0]
# 将项目的路径添通过软方法添加到环境变量中
sys.path.append(rootpath)
print('将整个项目的路径添通过软方法添加到环境变量中才能跨目录调用自定义的模块')
# 将需要在dos窗口执行的py文件的目录通过软方法添加到环境变量中，貌似可有可无
"""sys.path.append(curpath)
	print(sys.path)"""
import pytest
import time



if __name__ == '__main__':
	starttime = time.time()
	# 获得要执行测试的py文件
	# test_division/test_division01.py
	run_path = os.path.abspath(r'../mytestcase/')
	# pytest.main(['-v', r'E:\PycharmProjects\subline_pytest\mytestcase\test_add/test_add.py'])
	# 只执行标记了division02标记的测试用例
	#pytest.main(['-v','-s',run_path, "-m=division02"])
	# 不执行标记了division02标记的测试用例,执行其他用例
	# pytest.main(['-v','-s',run_path, "-m=not division02"])
	pytest.main(['-v','-s',run_path,'--html=../report/report.html'])
	#'-v:显示测试用例的函数名'
	# '-s:显示执行测试用例时的fixture的执行信息'
	speedtime = time.time() - starttime
	print(speedtime)
		
	
