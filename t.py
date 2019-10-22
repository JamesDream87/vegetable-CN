import requests
from lxml import html

def Main():
  soup = getHtml('http://www.vegnet.com.cn/Price/List?marketID=2&year=2019&month=10&day=17')
  ClearData(soup)

def getHtml(url):
  page=requests.Session().get(url) 
  tree=html.fromstring(page.text)
  return tree

def ClearData(soup):
  div = soup.xpath('//div[@class="Pager"]//a[last()]/text()')
  href = soup.xpath('//div[@class="Pager"]//a/@href')
  for each in div:
    each = each.__str__()
  
  next = []
  for each in range(len(href)):
    if(each < (len(href)-1)):
      next.append(href[each])

  print(next)
  
Main()