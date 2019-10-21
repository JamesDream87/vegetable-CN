import pandas as pd
import re

FileRes = True

def read_csv():
  try:
    with open('./dataset/market.csv'):
      df = pd.read_csv('./dataset/market.csv',index_col=0)
      FileRes = True
      return df

  except IOError as err:
    print('dont have the market.csv in dataset folder,please use the getMarket.run() fuction')
    FileRes = False

def to_json(df):
  print(df)

def to_list(df):
  print(df)

def run(type):
  df = read_csv()
  
  if(FileRes == True):
    if(type == 'list' or type == 'List'):
      data = to_list(df)
    elif(type == 'json' or type == 'Json'):
      data = to_json(df)
  
  else:
    print('dont have data')
    
  return data

run('list')