# -*- coding: utf-8 -*-
# @Time : 2019/6/18 20:46
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : dir_config.py
# @Software: PyCharm Community Edition
import  os
# 框架顶层目录
base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
testdatas_dir=os.path.join(base_dir,'TestDatas')
testcases_dir=os.path.join(base_dir,'TestCases')
htmlreport_dir=os.path.join(base_dir,'Ouptuts/reports')
logs_dir=os.path.join(base_dir,'Ouptuts/logs')
screenshot_dir=os.path.join(base_dir,'Ouptuts/screenshots')
print(screenshot_dir)