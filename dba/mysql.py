import pymysql


def insert_price(config, df):
  print(df)

def select_price(name, market):
  print(name)

def insert_market(config, df):
  # 创建数据库连接
  db = pymysql.connect(config['host'], config['user'], 
    config['password'], config['database'], charset='utf8mb4')
  # 将df数据插入数据库
  df.to_sql(name='market', con = config, if_exists = 'append', index=False)

def select_market(name):
  print(name)

def select_null_market(date):
  print(date)
