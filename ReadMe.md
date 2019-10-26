# 关于本项目
  中国蔬菜价格行情获取与分析工具

  [ENGLISH Version](ReadMe_EN.md)

## 使用到的库
  ```
    pip install pandas
    pip install lxml
    pip install requests
    pip install sqlalchemy
    pip install pymysql
  ```

## 关于SQL功能
  如果您需要使用到SQL功能，请在根目录内创建一个settings目录，然后创建
  一个config.py文件在settings目录内，按照以下格式填入您的MySQL信息。
  ```
    config ={     
      'host': 'your host',       
      'user': 'your user name',              
      'password': 'your password',       
      'port': 'your port number',                   
      'database': 'your db name'
    }
  ```

# 更新计划
  1.完善Analyze 分析模块
  2.完善dba 数据模块，实现更多的数据库使用方式
  3.完善文档