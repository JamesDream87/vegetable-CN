from market import getMarket as gm
from market import getData as gd
from price import getPrice as gp
from dba import mysql as ms
from settings import config
import pandas as pd

# idList, name = gm.run()
idList = gd.get_id_list()
name = gd.get_name_list()
df = {
  "ID": idList,
  "name": name,
}
df = pd.DataFrame(df)
ms.insert_market(config.config, df)