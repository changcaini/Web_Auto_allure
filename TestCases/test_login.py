# -*- coding: utf-8 -*-
# @Time : 2019/6/10 14:04
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : test_login.py
# @Software: PyCharm Community Edition
# 前程贷web网址：http://120.78.128.25:8765/Index/index
# 帐号/密码：18684720553、python
# 或者帐号密码：13760246701、python
import unittest
import ddt
from selenium import webdriver
from PO_V5.PageObjects.index_page import IndexPage
from PO_V4.PageObjects.login_page import LoginPage
from PO_V4.TestDatas import login_datas as ld
from PO_V4.TestDatas import Common_data as cd

# 用例三部曲：前置、步骤、断言
@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("{}/Index/login.html".format(cd.base_url))


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def tearDown(self):
        self.driver.refresh()

    # 1、错误数据
    @ddt.data(*ld.wrong_datas)
    def test_login_1_wrong_datas(self,data):
        LoginPage(self.driver).login(data["user"],data["password"])
        # 断言：页面提示内容为：请输入密码   //div[@class="form-error-info"]
        self.assertEqual(LoginPage(self.driver).check_invest_wrong_data_mes(),data["check"])
# 2、登录失败
    @ddt.data(*ld.fail_datas)
    def test_login_2_fail_datas(self, data):
        LoginPage(self.driver).login(data["user"], data["password"])
            # 断言：页面提示内容为：请输入密码   xpth='//div[@class="layui-layer-content"]'
        self.assertEqual(LoginPage(self.driver).check_invest_fail_mes(),data["check"])
        # 3、正常用例
    @ddt.data(ld.success_data)
    def test_login_3_success(self,data):
        # 步骤：登录操作——登录页面
        LoginPage(self.driver).login(data["user"], data["password"])
        # 断言：页面是否存在 我的账户 元素
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        # url跳转
        self.assertEqual(self.driver.current_url, ld.success_data["check"])
