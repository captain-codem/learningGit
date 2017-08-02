# -*- coding: utf-8 -*-
# @Time : 2017/1/1 17:51
# @Author : woodenrobot

#coding:utf-8
from scrapy import cmdline
name = 'xiaohuar'
cmd  = 'scrapy crawl {0}'.format(name)
print cmd.split()
cmdline.execute(cmd.split())
#cmdline.execute('scrapy parse --spider=MySpider -d 3 http://music.douban.com/chart')