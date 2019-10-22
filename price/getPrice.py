import requests
from lxml import html,etree
import pandas as pd
import datetime

# 初始化链接
def init(market, year, month, day):
  url = f'http://www.vegnet.com.cn/Price/List?marketID={market}&year={year}&month={month}&day={day}'
  return url

# 传入市场id，进行循环操作初始化
def loop(List):
  year = datetime.datetime.now().year
  month = datetime.datetime.now().month
  day = datetime.datetime.now().day

  for each in List:
    url = init(each, year, month, day)
    print(url)

#获取是否含有多页数据
def getHtml(url):
  page=requests.Session().get(url) 
  tree=html.fromstring(page.text)
  next = is_next(tree)
  print(next)


# 获取是否有下一页
def is_next(soup):
  # 是否含有下一页的文本标签
  # NextPage = soup.xpath('//div[@class="Pager"]//a[last()]/text()')

  href = soup.xpath('//div[@class="Pager"]//a/@href')
  next = []

  for each in range(len(href)):
    if(each < (len(href)-1)):
      next.append(href[each])
  
  return next