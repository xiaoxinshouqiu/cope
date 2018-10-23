#!/ifs9/BC_B2C_01A/B2C_SGD/SOFTWARES/anaconda3/bin/python
# -*- coding=utf-8 -*-

import configparser
import os
import re
import sys
import time

# for example:2018-10-09
# file before this date will be transfered
# file after this date will not be transfered
trans_date = sys.argv[1]
# for example:'/data/webdb/datafiles/20181008F12FHQHSSJ0877'
# the path that storages data
data_back = sys.argv[2]

# caculate MD5 and generate MD5.txt in this directory
# file is a dir name and an absolute path
def caculate_md5(file):
    os.chdir(file)
    all_file = os.listdir(file)
    # delete md5.txt before generating MD5.txt
    # and do not calculate MD5 of "MD5.txt"
    # in case of errors when checking MD5
    if os.path.exists(file+'/MD5.txt'):
        os.system('rm MD5.txt')
    for i in range(len(all_file)):
        if all_file[i] == 'MD5.txt':
            pass
        else:
            os.system('md5sum '+all_file[i]+' >>MD5.txt')


# This approach seems a bit stupid.
# →_→ →_→ →_→
# days = 365*year + 30*month + day 
def get_days(string):
    tmp = re.split('-',string)
    days = int(tmp[0])*365+int(tmp[1])*30+int(tmp[2])
    return days


# Parsing configuration file
# load_path--the raw data path
conf = configparser.ConfigParser()
with open('C:\\Users\\dongxinyu\\Desktop\\cp_data\\conf.ini','w') as fw:
    conf.write(fw)
load_path = conf.get('config','load_path')
os.chdir(load_path)
cp_data_path = conf.get('config','cp_data_path')

deadline = get_days(trans_date)
all_file = os.listdir(load_path)
for i in range(len(all_file)):
    file = all_file[i]
    if os.path.isdir(file):
        # get date that dir is created
        abs_path = load_path+file
        creat_date_NO = time.localtime(os.stat(file).st_ctime)
        creat_date = time.strftime("%Y-%m-%d", creat_date_NO)
        days = get_days(creat_date)
        if deadline - days > 0 :
            caculate_md5(abs_path)
            # cp_data is a shell script 
            # copy data to a remote sever
            # without inputing password manually
            os.system("%s %s %s" %(cp_data_path,abs_path, data_back))
        else:
            pass
