import requests
from lxml import html,etree
import pandas as pd
import time
import re

def getHTML(url):
  page=requests.Session().get(url) 
  tree=html.fromstring(page.text)
  Vname = tree.xpath('//div[@class="main gap"]//div[@class="skin_mar mar_list"]//text()')
  return Vname

def To_CSV(id, name):
  df = {
    "ID": id,
    "name": name,
  }
  df = pd.DataFrame(df)
  df.to_csv('./dataset/market.csv',index=False)


def run():
  id = 1
  name = []
  idList = []
  while(id<=497):
    url = f'http://www.vegnet.com.cn/Price/list_ar110000.html?marketID={id}'
    Vname = getHTML(url)
    
    for each in Vname:
      each = each.__str__()
      each = re.sub(r'\d',"",each)
      each = re.sub(r'[a-z]','',each)
      each = re.sub(r'\s','',each)

      if(each != ''):
        name.append(each)
        idList.append(id)
    
    print(f'id:{id}')
    id += 1

  To_CSV(idList, name)