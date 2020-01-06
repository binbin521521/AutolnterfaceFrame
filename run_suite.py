import unittest
from script.test_tpshop_login import TestTPShopLogin
import os
import time
from tools.HTMLTestRunner import HTMLTestRunner

# 1 初始化测试套件
suite = unittest.TestSuite()
# 2 添加测试用例到测试套件
suite.addTest(unittest.makeSuite(TestTPShopLogin))
# 3 生成测试报告路径和名称
# os.path.dirname(os.path(__file__))的意思就是获取当前执行文件的爸爸的目录
report_path = os.path.dirname(os.path.abspath(__file__)) + '/report/tpshop{}.html'.format(
    time.strftime('%Y%m%d %H%M%S'))
# 4 打开测试报告文件，初始化HTMLTestRunner,执行测试套件，生成测试报告
with open(report_path, 'wb')as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, title='TPShop登录接口测试', description='v1.0.0')
    # 使用初始化的runner实例运行测试套件生成测试报告
    runner.run(suite)
