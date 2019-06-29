# -*- coding: utf-8 -*-
# @Time : 2019/6/11 20:39
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : login_datas.py
# @Software: PyCharm Community Edition
# 测试数据
from class_web_20190606.PO_V1.TestDatas.Common_data import base_url
# 成功登录
success_data={"user":"18684720553","password":"python","check":"{}/Index/index".format(base_url)}
# 输入框提示
wrong_datas=[
    {"user":" ", "password": "python", "check": "请输入手机号"},
    # {"user":"18684720553","password":" ","check":"请输入密码"},
    # {"user":"1868472055", "password": "python", "check": "请输入正确的手机号"},
    {"user":"186847205530", "password": "python", "check": "请输入正确的手机号"}
]
# 3s提示
fail_datas=[
    {"user": "18684720555", "password": "python", "check": "此账号没有经过授权，请联系管理员!"},
    {"user": "18684720553", "password": "123", "check": "帐号或密码错误!"}
]
