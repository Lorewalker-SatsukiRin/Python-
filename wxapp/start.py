#Author: 游学者冴月麟
# -*- coding = utf-8 -8-
# @Site : 
# @File: start.py
# @Software: PyCharm
# @Time: 2020/6/23 14:01
from scrapy import cmdline

cmdline.execute("scrapy crawl wxapp_spider".split())
