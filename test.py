from market import getMarket as gm
from market import getData as gd
from price import getPrice as gp
from dba import mysql as ms
from settings import config
import pandas as pd
import datetime

# 插入市场信息
def insert_market():
  # idList, name = gm.run()
  idList = gd.get_id_list()
  name = gd.get_name_list()
  df = {
    "market_id": idList,
    "name": name,
  }
  df = pd.DataFrame(df)
  # print(df)
  ms.insert_market(config.config, df)

# 查询市场列表
def select_market():
  db_data = ms.select_market(config.config, '山东')
  for each in db_data:
    print(each.name)

# 插入市场价格信息
def insert_price():
  year = datetime.datetime.now().year
  month = datetime.datetime.now().month
  day = datetime.datetime.now().day - 1
  MarketNull = []
  List = gd.get_id_list()
  for each in List:
    url = gp.init(each, year, month, day)
    # 爬取网页信息返回未清理的参数
    Vdate,Vmarket,Vname,Vlow,Vhigh = gp.getHtml(url)

    # 判断是否为空数据，空数据就直接跳过本次循环
    if(len(Vname)<=0):
      print(f'本市场ID没有数据,:marketID:{each}')
      MarketNull.append(each)
      continue
    else:
      # 返回清理的参数
      date,mark,name,low,high = gp.ClearData(Vdate,Vmarket,Vname,Vlow,Vhigh)
      #转为dataframe
      df = {
        "date": date,
        "market_name": mark,
        "vegetable": name,
        "low": low,
        "high": high
      }
      df = pd.DataFrame(df)
      # print(df)
      ms.insert_price(config.config, df)
  
  # 将没有数据的ID对应名称后存入数据库
  #insert_NULL_Market(MarketNull)

# 插入空数据的Market
def insert_NULL_Market(MarketNull):
  NullName = []
  nameList = gd.get_json()
  for each in MarketNull:
    for j in nameList:
      if(each == j['ID']):
        NullName.append(j['name'])

  ef = {
    'market_id': MarketNull,
    'name': NullName
  }

  ef = pd.DataFrame(ef)
  ms.insert_null_market(config.config, ef)

# 查询价格
def select_vege_price(name, date):
  data = ms.select_price(config.config, name, date)
  for each in data:
    print(f'市场名：{each.market_name},最低价:{each.low},最高价：{each.high}')

def delete_null_market():
  temp_id = []
  have_id = []
  null = ms.select_null_market(config.config)
  for each in null:
    temp_id.append(each.market_id)
  
  market_id = gd.get_id_list()
  # 差集
  have_id = list(set(market_id).difference(set(temp_id)))
  have_name = []
  market_name = gd.get_json()
  for each in market_name:
    for j in have_id:
      if(j == each['ID']):
        have_name.append(each['name'])

  df = {
    "ID": have_id,
    "name": have_name,
  }
  df = pd.DataFrame(df)
  df.to_csv('dataset/market.csv',index=True)

insert_price()