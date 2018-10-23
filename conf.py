# -*- coding=utf-8 -*- #

import configparser

# 加载现有的配置文件
conf = configparser.ConfigParser()
# 写入配置文件
# 添加section
conf.add_section('config')
# 添加值
value1 = '/ifs7/B2C_SGD/PROJECT/BGISEQ-500_Project/upload/dataEveryWeek/Upload/'
conf.set('config', 'load_path', value1 )
value2 = 'ifs7/B2C_SGD/USER/xydong/mature_script/cp_data'
conf.set('config', 'cp_data_path', value2)

# 写入文件
with open('C:\\Users\\dongxinyu\\Desktop\\cp_data\\conf.ini','w') as fw:
    conf.write(fw)

# 读取配置文件
load_path = conf.get('config', 'load_path')
cp_data_path = conf.get('config', 'cp_data_path')
print ('load_path:',load_path)
print ('load_path:',cp_data_path)