# -*- coding: utf-8 -*-
# @Time : 2019/6/23 10:03
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : login_page_locator.py
# @Software: PyCharm Community Edition
from selenium.webdriver.common.by import By
class LoginPageLocator():
    # 用户名
    use_loc=(By.XPATH,'//input[@name="phone"]')
    # 密码
    passwd_los=(By.XPATH,'//input[@name="password"]')
    # 登录按钮
    login_button_loc=(By.XPATH,'//button')
    # 输入框提示
    error_notify_from_loginForm = (By.XPATH, '//div[@class="form-error-info"]')
    # 提示框 - 页面中间区域
    error_notify_from_pageCenter = (By.XPATH, '//div[@class="layui-layer-content"]')