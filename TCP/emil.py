"""
----------------------------------------
    File Name: emil
    Author: Kong
    Date: 2021/8/3
    Description: 
----------------------------------------
"""
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = '1939667131@qq.com'
    receivers = ['kongfanyue0924@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('孔凡跃', 'utf-8')
    message['To'] = Header('kong', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.126.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'KFY5217KFY')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()