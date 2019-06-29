# -*- coding: utf-8 -*-
# @Time : 2019/6/23 14:52
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : user_page.py
# @Software: PyCharm Community Edition

from PO_V4.Common.basepage import BasePage
from PO_V4.PageLocators.userPage_locator import UserPageLocator as loc
class UserPage(BasePage):
    def get_user_leftMoney(self):
        doc='个人页面——获取用户余额'
        self.wait_eleVisible(loc.user_lefMoney,doc)
        # 获取文本值
        text=self.get_element_text(loc.user_lefMoney,doc)
        return text.strip("元")


