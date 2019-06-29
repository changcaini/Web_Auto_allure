# -*- coding: utf-8 -*-
# @Time : 2019/6/18 20:15
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : main.py
# @Software: PyCharm Community Edition

# 记录一下用例执行过程——
# 如果用例失败——Trackback报错信息——失败截图
# 记录用例的执行时间-起始，等待，结束提供测试报告
# 用例、页面对象当中，用例=页面对象+测试数据
# 断言失败了，页面对象方法执行的时候报错了
# alert切换，iframe切换，下拉列表、上传

import pytest

pytest.main(["-m","login","--alluredir=Outputs/allure_reports"])
# pytest -v -s --alluredir=Outputs/allure_reports