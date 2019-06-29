# -*- coding: utf-8 -*-
# @Time : 2019/6/18 20:27
# @Author : "CCN"
# @Email : 869548371@qq.com
# @File : basepage.py
# @Software: PyCharm Community Edition
import  logging
from PO_V5.Common.dir_config import screenshot_dir
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import time


class BasePage:
    # 包含了PageObject中用到的底层方法
    def __init__(self, driver):
        self.driver = driver
 # 1、等待元素可见
    def wait_eleVisible(self,loc,img_doc="",timeout=60,freguency=0.1):
        logging.info("等待{0}元素可见".format(loc))
        try:
            #起始等待的时间
            start=datetime.datetime.now()
            WebDriverWait(self.driver,timeout,freguency).until(EC.visibility_of_all_elements_located(loc))
        # 结束等待时间
            end = datetime.datetime.now()
            logging.info("开始等待时间:{0}，结束等待时间：{1}，等待时长：{2}".format(start,end,end-start))
        except:
        # 日志
         logging.exception("等待元素可见失败：")
        # 截图，哪一个页面哪个操作导致失败
         self.save_web_screenshot(img_doc)

    #2、查找一个元素
    def get_element(self,loc,img_doc=""):
       logging.info("查找{}中的元素{}".format(loc,img_doc))
       try:
           ele=self.driver.find_element(*loc)
           return ele
       except:
           # 日志
           logging.exception("查找元素失败 ")
           # 截图
           self.save_web_screenshot(img_doc)
           raise
    # 3、点击元素
    def click_element(self,loc,img_doc,timeout=30,frquence=0.5):
       # 3-1等待元素可见
       self.wait_eleVisible(loc,img_doc,timeout,frquence)
       # 3-2先找元素
       ele=self.get_element(loc,img_doc)
       # 3-3再操作
       logging.info("点击元素{}".format(loc))
       try:
           ele.click()
       except:
           logging.info("点击元素失败")
           self.save_web_screenshot(img_doc)
           raise
    # 4、输入文本值
    def input_text(self, loc, img_doc, *args):
       # 等待元素可见
       self.wait_eleVisible(loc,img_doc)
       # 查找元素
       ele=self.get_element(loc,img_doc)
       # 再操作
       logging.info("给元素{}输入文本值{}".format(loc,args))
       try:
           ele.send_keys(*args)
       except:
           logging.info("元素输入失败")
           self.save_web_screenshot(loc)
           raise
    # 5、获取元素的属性值
    def get_element_attribute(self,loc,attr_name, img_doc):
      ele = self.get_element(loc, img_doc)
      # 再操作
      try:
          value=ele.get_attribute(attr_name)
          logging.info("获取元素{}的属性{}值{}".format(loc, attr_name, value))
          return value
      except:
          logging.info("获取元素属性值失败")
          self.save_web_screenshot(img_doc)
          raise
# 6、获取元素的文本值
    def get_element_text(self,loc,img_doc):
        ele=self.get_element(loc,img_doc)
        try:
            text=ele.text
            logging.info("获取元素{}的文本值{}".format(loc,text))
            return text
        except:
            logging.info("获取文本值失败")
            self.save_web_screenshot(img_doc)
            raise

        # 7、网页截图
    def save_web_screenshot(self, img_doc):
            # 文件名不能带特殊符号
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            # 图片根目录+页面+功能名称+时间。png
            filepath = "{}_{}.png".format(img_doc, now)
            try:
                self.driver.save_screenshot(screenshot_dir + "/" + filepath)
                logging.info("网页截图成功，图片存储在：{}".format(screenshot_dir + "/" + filepath))
            except:
                logging.exception("网页截图失败")
