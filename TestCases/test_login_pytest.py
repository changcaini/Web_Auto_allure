# -*- coding: utf-8 -*-
# @Time : 2019/6/24 21:58
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : test_login_pytest.py
# @Software: PyCharm Community Edition

from PO_V5.PageObjects.index_page import IndexPage
from PO_V5.PageObjects.login_page import LoginPage
from PO_V5.TestDatas import login_datas as ld
import pytest
import allure

# 用例三部曲：前置、步骤、断言
@pytest.mark.usefixtures("open_url")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    pytestmark=pytest.mark.login  # 整个TestLogin类里面，所有测试用例都有
    # 1、错误数据
    @pytest.mark.parametrize("data", ld.wrong_datas)
    def test_login_1_wrong_datas(self,data,open_url):
        LoginPage(open_url).login(data["user"],data["password"])
        # 断言：页面提示内容为：请输入密码   //div[@class="form-error-info"]
        assert LoginPage(open_url).check_invest_wrong_data_mes()==data["check"]
# 2、登录失败
    @pytest.mark.parametrize("data",ld.fail_datas)
    def test_login_2_fail_datas(self, data,open_url):
        LoginPage(open_url).login(data["user"], data["password"])
            # 断言：页面提示内容为：请输入密码   xpth='//div[@class="layui-layer-content"]'
        tips=LoginPage(open_url).check_invest_fail_mes()
        print(tips)
        assert tips==data["check"]

        # 3、正常用例
    # @pytest.mark.parametrize("data",ld.success_data)
    @pytest.mark.smoke
    def test_login_3_success(self,open_url):
        # 步骤：登录操作——登录页面
        LoginPage(open_url).login(ld.success_data["user"], ld.success_data["password"])
        # 断言：页面是否存在 我的账户 元素
        assert IndexPage(open_url).check_nick_name_exists()==True
        # url跳转
        assert open_url.current_url==ld.success_data["check"]