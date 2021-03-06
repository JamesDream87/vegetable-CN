import pandas as pd
import json

def read_csv():
  res = True
  try:
    with open('./dataset/market.csv'):
      df = pd.read_csv('./dataset/market.csv',index_col=0)
      FileRes = True
      return df,res

  except IOError as err:
    print('dont have the market.csv in dataset folder,please use the getMarket.run() fuction')
    res = False
    return None,res

def set_json():
  df,res = read_csv()
  if(res == True):
    df_json = df.to_json(orient = 'records', force_ascii = False)
    fo = open("./dataset/market.json", "w", encoding='utf-8')
    fo.write(df_json)
  else:
    print('have not data')

def get_json():
  fo = open("./dataset/market.json", encoding='utf-8')
  data = json.loads(fo.read())
  return data

def get_id_list():
  df,res = read_csv()
  if(res == True):
    data = df.ID.values
    return data
  else:
    print('have not data')

def get_name_list():
  df,res = read_csv()
  if(res == True):
    data = df.name.values
    return data
  else:
    print('have not data')
