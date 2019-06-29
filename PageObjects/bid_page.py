# -*- coding: utf-8 -*-
# @Time : 2019/6/14 22:07
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : invest_page.py
# @Software: PyCharm Community Edition


# 选择标：/html/body/div[4]/div[1]/div[2]/div[1]/div[3]/div/a

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PO_V4.Common.basepage import BasePage
# from PO_V4.PageLocators.indexPage_locator import IndexPageLocator as loc
from PO_V4.PageLocators.bidPage_locator import BidPageLocator as loc
import time

class BidPage(BasePage):
    def invest(self,money):
        # 投资金额输入框
       self.input_text(loc.money_input,'标页面_输入投资金额',money)
        #点击投标按钮：  //button[@class="btn btn-special height_style"]
       self.click_element(loc.invest_button,'标页面_投资按钮')

    # 查询用户余额
    def user_amount(self):
        # // div[@class ="clearfix left"] / input
        self.wait_eleVisible(loc.money_input,'标页面——获取用户余额')
        amount=self.get_element_attribute(loc.money_input,'data-amount','标页面——获取用户余额')
        return amount

    # 投资成功的提示框 - 点击查看并激活
    def click_activeButton_on_success_popup(self):
        doc='标页面——投资成功提示 '
        self.wait_eleVisible(loc.active_button_on_successPop,doc)
        self.click_element(loc.active_button_on_successPop,doc)

    # 错误提示框 - 页面中间
    def get_errorMsg_from_pageCenter(self):
        self.wait_eleVisible(loc.invest_failed_popup,'标页面——投资失败3S提示')
        msg=self.get_element_text(loc.invest_failed_popup,'标页面——投资失败提示')
        self.click_element(loc.invest_close_failed_popup_button,'标页面——关闭失败提示框')
        return msg
