#!/usr/bin/expect


#-1是不限制超时时间
set timeout -1
#需要传输的文件夹
set file_name [lindex $argv 0]
#远程登陆
spawn scp -r $file_name zhoulijun@192.168.8.66
expect "*password:"
send "C9yiM4dy0QMT"
send ""
expect eof