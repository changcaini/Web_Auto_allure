# -*- coding: utf-8 -*-
# @Time : 2019/6/23 13:55
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : indexPage_locator.py
# @Software: PyCharm Community Edition
from selenium.webdriver.common.by import By
class IndexPageLocator:
    # 关于我们
    about_us=(By.XPATH,'//a[text()="关于我们"]')
    # 用户名
    user_link=(By.XPATH,'//a[@href="/Member/index.html"]')
    # 抢投标按钮
    bid_button=(By.XPATH,'//a[@class="btn btn-special"]')