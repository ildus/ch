#coding: utf-8

import sys
import os
def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chtoru',
        'PASSWORD':'21452',
        'USER':'root',
        'SUPPORTS_TRANSACTIONS':True,
    }
}

"""
    Отправка почты
"""
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yaxa.post@gmail.com'
EMAIL_HOST_PASSWORD = '2145221452'
EMAIL_FROM = 'yaxa.ru'
EMAIL_REPLY = 'yaxa.post@gmail.com'

LOCAL = True