import requests
from lxml import html,etree
import pandas as pd
import datetime

# 初始化链接
def init(market, year, month, day):
  url = f'http://www.vegnet.com.cn/Price/List?marketID={market}&year={year}&month={month}&day={day}'
  print(f'正在执行MarketId:{market}')
  return url

# 传入市场id，进行循环操作初始化
def loop(List):
  year = datetime.datetime.now().year
  month = datetime.datetime.now().month
  day = datetime.datetime.now().day
  MarketNull = []
  for each in List:
    url = init(each, year, month, day)
    # 爬取网页信息返回未清理的参数
    Vdate,Vmarket,Vname,Vlow,Vhigh = getHtml(url)
    # 判断是否为空数据，空数据就直接跳过本次循环
    if(len(Vname)<=0):
      print('本市场ID没有数据')
      MarketNull.append(each)
      df = {
        "MarketId": MarketNull
      }
      df = pd.DataFrame(df)
      df.to_csv(f'./dataset/MarketNULL.csv',index=False)

    else:
      # 返回清理的参数
      date,mark,name,low,high = ClearData(Vdate,Vmarket,Vname,Vlow,Vhigh)
      # 转为csv
      df = {
        "日期": date,
        "市场名称": mark,
        "蔬菜名": name,
        "最低价": low,
        "最高价": high
      }
      df = pd.DataFrame(df)
      df.to_csv(f'./dataset/price-{each}-{year}{month}{day}.csv',index=False)

#获取是否含有多页数据
def getHtml(url):
  page=requests.Session().get(url) 
  soup=html.fromstring(page.text)
  Vdate,Vmarket,Vname,Vlow,Vhigh = setData(soup)
  # 获取是否有下一页信息
  next = is_next(soup)
  # 如果存在下一页信息
  if(len(next) > 0):
    print('发现分页内容，正在检索')
    for each in next:
      page=requests.Session().get(f'http://www.vegnet.com.cn/{each}') 
      soup=html.fromstring(page.text)
      Ddata,Dmarket,Dname,Dlow,Dhigh = setData(soup)
      Vdate.extend(Ddata)
      Vmarket.extend(Dmarket)
      Vname.extend(Dname)
      Vlow.extend(Dlow)
      Vhigh.extend(Dhigh)
  
  #将数据整理为一定的格式
  return Vdate,Vmarket,Vname,Vlow,Vhigh

# 筛选出数据
def setData(soup):
  Vdate = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_1"]/text()')
  Vmarket = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_3"]//a/text()')
  Vname = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][1]/text()')
  Vlow = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][2]/text()')
  Vhigh = soup.xpath('//div[@class="pri_k"]//p//span[@class="k_2"][3]/text()')

  return Vdate,Vmarket,Vname,Vlow,Vhigh

def ClearData(Vdate,Vmarket,Vname,Vlow,Vhigh):
  date = []
  high = []
  low = []
  mark = []
  name = []

  for each in Vdate:
    each = each.__str__()
    each = each.strip('[')
    each = each.strip(']')
    date.append(each)

  for each in Vmarket:
    mark.append(each)
  
  for each in Vname:
    name.append(each)

  for each in Vlow:
    each = each.strip('¥')
    low.append(each)

  for each in Vhigh:
    each = each.strip('¥')
    high.append(each)

  return date,mark,name,low,high

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
