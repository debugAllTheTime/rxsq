# coding:utf-8
import requests
import json
import time
from datetime import date, timedelta
from lxml import etree
import execjs
import os
from email.mime.text import MIMEText
import smtplib





# 一卡通号、密码、姓名、手机号、身份证号等个人信息
username = os.environ["username"]
password = os.environ["password"]
USER_NAME = os.environ["USER_NAME"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
ID_NO = os.environ["ID_NO"]

# 行程卡信息
scope = '162052471086425'
filetoken = scope+'1'


#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.seu.edu.cn'  
#163用户名
mail_user = username+'@seu.edu.cn'  
#密码(部分邮箱为授权码) 
mail_pass = password
#邮件发送方邮箱地址
sender = username+'@seu.edu.cn'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['774040105@qq.com'] 






tomorrow_year = (date.today() + timedelta(days=1)).strftime("%Y")
tomorrow_month = (date.today() + timedelta(days=1)).strftime("%m")
tomorrow_day = (date.today() + timedelta(days=1)).strftime("%d")
tomorrow_date = str(tomorrow_year)+"-"+str(tomorrow_month)+"-"+str(tomorrow_day)
#print(startFlow_response.text)
subject = str(tomorrow_date)
subject = subject+'入校申请\t成功'
msg = str(tomorrow_date)+'入校申请成功'







#设置email信息
#邮件内容设置
message = MIMEText(msg,'plain','utf-8')
#邮件主题       
message['Subject'] = '打卡成功' 
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0]  
try:
    smtpObj = smtplib.SMTP() 
    #######替换为########
    smtpObj = smtplib.SMTP_SSL(mail_host,port=465)   
    #登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    #发送
    smtpObj.sendmail(
        sender,receivers,message) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误
