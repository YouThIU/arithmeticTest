import pytest
import os
from selenium import webdriver
from py.xml import html
from datetime import datetime

driver = None
# 使用编程方式注册标记。全局有效.用于@pytest.mark.MARKNAME
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "division02: is an optional description."
    )

  # 添加命令行参数
  # 命令行参数：根据命令行选项将不同的值传递给参数用例。 
  #'1：在conftest.py文件中添加命令行选项，其中命令行参数为：--cmdopt'
  #'2:用于@pytest.fixture。可以直接得到命令行参数的值：request.config.getoption('--cmdopt')'
def pytest_addoption(parser):
	parser.addoption(
  		'--cmdopt',action='store', default='type1',
  		help='my option:type1 or type2'
  		)

@pytest.fixture(scope='session', autouse=True)
def autouse_session():
  print('autouse为True，session执行一次；开始执行')
  yield
  print('autouse为True，session执行一次；结束执行')


@pytest.fixture()
def browser():
  global driver
  if driver is None:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
  return driver

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
  """钩子函数，给测试报告的table添加两列 删除最后一列"""
  cells.insert(2, html.th('Description'))
  #cells.insert(3, html.th('Test_nodeid'))
  cells.insert(1, html.th('Time', class_='sortable time', col='time'))
  cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
  # 源码中获取用例的docstring的方式
  """给两列添加详情，并删除最后一列"""
  cells.insert(2, html.td(report.description))
  # 源码中获取用例的nodeid方式，在TestResult类中
  #cells.insert(3, html.td(report.nodeid))
  cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
  cells.pop()
  '''从报告中删除测试通过的结果
  if report.passed:
    del cells[:]'''

@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):  
# 从报告中清空测试通过的日志输出
  if report.passed:
    data.append(html.div('No log output captured', class_='empty log'))


# 用例失败截图，保存在测试报告中（report.html）
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
  """当测试失败的时候，自动截图，展示到html中"""
  pytest_html = item.config.pluginmanager.getplugin('html')
  outcome = yield
  report = outcome.get_result()
  # 返回一个对象属性值
  extra = getattr(report, 'extra', [])
  if report.when == 'call' or report.when == 'setup':
    xfail = hasattr(report, 'wasxfail')
    if (report.skipped and xfail) or (report.failed and not xfail):
      file_path = report.nodeid.replace('::', '_') + '.png'
      image_path = _capture_screenshot(file_path)
      print('loction',image_path)
      if file_path:
        html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % image_path
        extra.append(pytest_html.extras.html(html))
    report.extra = extra
  # 在报告中展示用例的docstring
  report.description = str(item.function.__doc__)
  # 先编码，在转码
  report.nodeid = report.nodeid.encode('utf-8').decode('unicode_escape')

def _capture_screenshot(path):
  """截图并且返回图片的路径"""
  # print(path)
  file_list = path.split('/')
  project_name = file_list[0]
  img_file_name = file_list[1]
  img_name = file_list[2]
  cur_path = os.path.dirname(os.path.abspath(__file__))
  # 使用join方法拼接路径时，参数不要有‘\’，直接写入目录名即可
  img_testcase_path = os.path.join(cur_path, project_name, img_file_name, 'image')
  if not os.path.isdir(img_testcase_path):
    """如果用例的截图目录不存在，就新建一个"""
    os.mkdir(img_testcase_path)
  # 用例失败的截图的路径
  img_path = os.path.join(img_testcase_path, img_name)
  driver.get_screenshot_as_file(img_path)
  return img_path

