# coding=utf-8

import unittest
import HTMLTestRunner
import os
import time

# 定义输出的文件位置和名字
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = report_path + now + "HtmlTemplate.html"

if __name__ == '__main__':
    suite = unittest.TestLoader().discover("testsuites")

    with open(HtmlFile, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'测试报告', description=u'执行情况', verbosity=1)
        runner.run(suite)
