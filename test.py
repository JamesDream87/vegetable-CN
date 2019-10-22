from market import getData as gd
from price import getPrice as gp

List = gd.get_id_list()
gp.loop(List)