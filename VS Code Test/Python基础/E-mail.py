from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = '2252175358@qq.com'
    receivers = ['fhy.sdwh@gmail.com', 'yzy.sdwh@gmail.com']
    message = MIMEText('用Python发送邮件的示例代码。', 'plain', 'utf-8')
    message['Form'] = Header('Fhy', 'utf-8')
    message['To'] = Header('Yzy', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')

    smtper.login(sender, 'suvueknalyijebgf')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成！')

if __name__ == "__main__":
    main()
    
