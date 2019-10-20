import requests
from lxml import html,etree
import pandas as pd

def Main():
  soup = getHtml('http://www.vegnet.com.cn/Price/List?marketID=342&year=2019&month=10&day=17')
  ClearData(soup)

def getHtml(url):
  page=requests.Session().get(url) 
  tree=html.fromstring(page.text)
  return tree

def ClearData(soup):
  date = []
  high = []
  low = []
  mark = []
  name = []
  div = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_1"]/text()')
  market = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_3"]//a/text()')
  Vname = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][1]/text()')
  Vlow = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][2]/text()')
  Vhigh = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][3]/text()')

  for each in div:
    each = each.__str__()
    each = each.strip('[')
    each = each.strip(']')
    date.append(each)

  for each in market:
    mark.append(each)
  
  for each in Vname:
    name.append(each)

  for each in Vlow:
    each = each.strip('¥')
    low.append(each)

  for each in Vhigh:
    each = each.strip('¥')
    high.append(each)

  df = {
    "日期": date,
    "市场名称": mark,
    "蔬菜名": name,
    "最低价": low,
    "最高价": high
  }
  df = pd.DataFrame(df)
  df.to_csv('Result.csv',index=False)

Main()