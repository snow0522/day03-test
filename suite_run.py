import unittest
import time
from HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scrips")
report_file = "./report/{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_file,"wb")as f:
    runner = HTMLTestRunner(stream=f,title="员工管理测试报告")
    runner.run(suite)