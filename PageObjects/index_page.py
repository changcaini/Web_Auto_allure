# -*- coding: utf-8 -*-
# @Time : 2019/6/10 13:32
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : index_page.py
# @Software: PyCharm Community Edition
import unittest
from selenium import webdriver
from PO_V4.PageObjects.login_page import LoginPage
from PO_V4.Common.basepage import BasePage
from PO_V4.PageLocators.indexPage_locator import IndexPageLocator as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class IndexPage(BasePage):
    # 1、页面正常跳转
    def check_nick_name_exists(self):
        WebDriverWait(self.driver,50).until(EC.visibility_of_all_elements_located((By.XPATH,'//a[text()="关于我们"]')))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True
        except:
            return False
    # 选择标的，点击抢投标
    def click_invest_button(self):
        doc='投资页面——抢投标按钮'
        self.wait_eleVisible(loc.bid_button,doc)
        self.click_element(loc.bid_button,doc)



