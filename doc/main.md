# 使用本程序
在根目录创建一个python文件，并引入各个模块，进行调用
例如创建一个Main.py然后倒入需要的模块

# 根据你所需的功能编写代码
详情可参考根目录的test.py
```
  from dba import mysql as ms

  # 查询市场列表
  def select_market():
    db_data = ms.select_market(config.config, '山东')
    for each in db_data:
      print(each.name)
```