# -*- coding: utf-8 -*-
# @Time : 2019/6/14 21:50
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : invest_datas.py
# @Software: PyCharm Community Edition
success_datas=[{"invest_amount":"100","check":"投资成功"}]
fail_datas=[
{"invest_amount":"10","check":"投标金额必须为100的倍数"},
# {"invest_amount":"12","check":"请输入10的整数倍"},
{"invest_amount":"0","check":"请正确填写投标金额"},
{"invest_amount":"-10","check":"请正确填写投标金额"},
{"invest_amount":"650000","check":"投标金额大于可用金额"}
]

wrong_datas=[{"invest_amount":"12","check":"请输入10的整数倍"}]

print(success_datas[0]["invest_amount"])
