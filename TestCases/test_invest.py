# -*- coding: utf-8 -*-
# @Time : 2019/6/13 20:05
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : test_invest.py
# @Software: PyCharm Community Edition
import unittest
import ddt
from selenium import webdriver
from PO_V4.PageObjects.index_page import IndexPage
from PO_V4.PageObjects.bid_page import BidPage
from PO_V4.PageObjects.login_page import LoginPage
from PO_V4.PageObjects.user_page import UserPage
from PO_V4.TestDatas import login_datas as ld
from PO_V4.TestDatas import Common_data as cd
from PO_V4.TestDatas import invest_datas as vd
import time
import logging
@ddt.ddt
class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("{}/Index/login.html".format(cd.base_url))
        # 正常登录
        LoginPage(cls.driver).login(ld.success_data["user"], ld.success_data["password"])
        # 选择标的，点击进入标页面
        IndexPage(cls.driver).click_invest_button()
        cls.bid_page=BidPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        logging.info("——————用例类后置：关闭浏览器会话,清理环境——————")
        cls.driver.quit()
    def tearDown(self):
        logging.info("——————每一个用例类后置：刷新当前页面——————")
        self.driver.refresh()
        time.sleep(5)

    # 投资失败
    @ddt.data(*vd.fail_datas)
    def test01_invest_fail_data(self, data):
        logging.info("——————投资用例：异常场景——————")
        BidPage(self.driver).invest(data["invest_amount"])
        # print('提示语：', IndexPage(self.driver).check_invest_fail_mes())
        # print('断言：', data["check"])
        errorMsg=BidPage(self.driver).get_errorMsg_from_pageCenter()
        assert errorMsg==data["check"]

   # 投资成功
    @ddt.data(vd.success_datas)
    def test02_invest_success(self,data):
            # data=vd.success_datas
            logging.info("*********投资用例：正常场景-投资成功*********")
            # 查询投资前用户余额
            before =self.bid_page.user_amount()
            print('berore:', before)
            # 投资
            self.bid_page.invest(int(data[0]["invest_amount"]))
            # 点击投资成功的激活按钮
            self.bid_page.click_activeButton_on_success_popup()
            print('投资金额：', data[0]["invest_amount"])
            # 投资后用户余额
            after =UserPage(self.driver).get_user_leftMoney() # 投资后用户余额
            print('after:', after)
            print(type(before),type(after),type(data[0]["invest_amount"]))
            sub_amount = float(before)-float(after)
            print('减少金额：', sub_amount)
            # 断言：投资前用户余额-投资后用户余额=投资金额
            self.assertEqual(sub_amount, float(data[0]["invest_amount"]))



