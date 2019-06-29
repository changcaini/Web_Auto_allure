# -*- coding: utf-8 -*-
# @Time : 2019/6/23 9:02
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : loggor.py
# @Software: PyCharm Community Edition
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from PO_V5.Common import dir_config

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'
handler_1=logging.StreamHandler()
curTime=time.strftime("%Y-%m-%d %H%M", time.localtime())
handler_2=RotatingFileHandler(dir_config.logs_dir+"Web_AutoTest_{0}.log".format(curTime),backupCount=20, encoding='utf-8')
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
logging.info("ccn")