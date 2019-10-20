import requests
from lxml import html,etree
import pandas as pd
import time

def Main():
  id = 1
  name = []
  idList = []
  while(id<=2000):
    url = f'http://www.vegnet.com.cn/Price/list_ar110000.html?marketID={id}'
    soup = getHtml(url)
    Vname = ClearData(soup)
    if(Vname != ''):
      name.append(Vname)
      idList.append(id)

    id += 1
    time.sleep(5)
  

def getHtml(url):
  page=requests.Session().get(url) 
  tree=html.fromstring(page.text)
  return tree

def  ClearData(soup):
  Vname = soup.xpath('//div[@class="main gap"]//div[@class="skin_mar mar_list"]//text()')
  Vname = Vname.__str__()
  return Vname

Main()

def To_CSV(id, name):
  df = {
    "市场id": id,
    "市场名称": name,
  }
  df = pd.DataFrame(df)
  df.to_csv('market.csv',index=False)