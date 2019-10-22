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
    getHtml(url)

#获取是否含有多页数据
def getHtml(url):
  page=requests.Session().get(url) 
  soup=html.fromstring(page.text)
  Vdata,Vmarket,Vname,Vlow,Vhigh = setData(soup)
  next = is_next(soup)
  if(len(next) > 0):
    for each in next:
      page=requests.Session().get(f'http://www.vegnet.com.cn/{each}') 
      soup=html.fromstring(page.text)
      Ddata,Dmarket,Dname,Dlow,Dhigh = setData(soup)
      Vdata.extend(Ddata)
      Vmarket.extend(Dmarket)
      Vname.extend(Dname)
      Vlow.extend(Dlow)
      Vhigh.extend(Dhigh)
  


def setData(soup):
  Vdata = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_1"]/text()')
  Vmarket = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_3"]//a/text()')
  Vname = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][1]/text()')
  Vlow = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][2]/text()')
  Vhigh = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][3]/text()')

  return Vdata,Vmarket,Vname,Vlow,Vhigh



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