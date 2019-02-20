# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:30:20 2018

@author: Admin
"""
import re
import urllib.request
import pymongo

class MaoyanSpider:
    def __init__(self):
        self.baseurl='https://maoyan.com/board/4?offset='
        self.headers={'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        self.offset=0
        #创建对象
        self.conn=pymongo.MongoClient('0.0.0.0',27017)
        self.db = self.conn['MaoDB']
        self.myset = self.db['film']
        
    #获取页面
    def getPage(self,url):
        req=urllib.request.Request(url,headers=self.headers)
        res=urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        self.parsePage(html)
    
    #解析页面
    def parsePage(self,html):
        #创建编译对象
        p=re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rList = p.findall(html)
        self.writeTomongo(rList)
    
    
    #保存数据
    def writeTomongo(self,rList):
        for r in rList:
            d={
                'name':r[0].strip(),
                'star':r[1].strip(),
                'releasetime':r[2].strip()
            }
            self.myset.insert(d)
        print("ok")
    
    
    
    def workOn(self):
        while True:
            c = input("爬取按y,退出按q")
            if c.strip().lower()=='y':
                
                url=self.baseurl+ str(self.offset)
                self.getPage(url)
                self.offset+=10
            else:
                print("爬取结束")
                break
        
        
        
        
if __name__=='__main__':
    spider=MaoyanSpider()
    spider.workOn()



























