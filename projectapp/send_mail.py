import os
from django.core.mail import send_mail
os.environ['DJANGO_SETTINGS_MODULE'] = 'mproject.settings'
def sendmail(b,c):
    # if __name__ == '__main__':
    send_mail(
        '您的注册邮箱验证码',
        '邮箱验证码：'+b,
        'yhjhgou@sina.com',
        [c],
        )
    return 'ok'
# sendmail('1234566')