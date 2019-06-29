# -*- coding: utf-8 -*-
# @Time : 2019/6/10 13:26
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : login_page.py
# @Software: PyCharm Community Edition
# 一个用例，一次浏览器的打开和结束
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PO_V4.PageLocators.login_page_locator import LoginPageLocator as loc
from PO_V4.Common.basepage import BasePage
import time

class LoginPage(BasePage):
    # 登录功能
    def login(self,user,password):
        # 输入用户名
        self.input_text(loc.use_loc, '登录——输入用户名', user)
        # 输入密码
        self.input_text(loc.passwd_los, '登录——输入密码', password)
        # 点击登录
        self.click_element(loc.login_button_loc,'登录——登录按钮')

    # 投资金额错误提示
    def check_invest_wrong_data_mes(self):
        self.wait_eleVisible(loc.error_notify_from_loginForm,'获取输入框提示失败')
        tips = self.get_element_text(loc.error_notify_from_loginForm, '输入框提示')
        return tips

    # 投资失败3S提示
    def check_invest_fail_mes(self):
        self.wait_eleVisible(loc.error_notify_from_pageCenter,'获取3S提示失败')
        tips=self.get_element_text(loc.error_notify_from_pageCenter,'3S 提示')
        return tips