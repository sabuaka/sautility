# -*- coding: utf-8 -*-
import sys
import json
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

class gmail(object):
    '''Gmail送信(２段階認証対応版)モジュール'''
    # パスワードは、Googleのアカウントにてアプリパスワードを取得して使用してください。
    # 参考：https://support.google.com/mail/answer/185833?hl=ja

    @staticmethod
    def get_login_info(file_name='prm_gmail_login.json'):
        '''ログイン情報をパラメーターファイル(json)から取得する'''
        result = False
        res_user = None
        res_password = None
        try:
            login_info = json.load(open(file_name, 'r'))
            res_user = login_info["user"]
            res_password = login_info["password"]
            result = True
        except:
            res_user = None
            res_password = None
            result = False
        return result, res_user, res_password

    def __init__(self, user, password):
        '''イニシャライザ'''
        self.mail_user = user  
        self.mail_pass = password
        self.mail_addr = user       # Gmailのログインユーザー名は自分のアドレス

    def send_mail(self, to_addrs:[], subject, body, sub_type='plain'):
        '''メールの送信'''
        # パラメータの設定
        smtp_server = 'smtp.gmail.com'
        port = 587
        from_addr = self.mail_addr
        encoding = 'utf-8'

        # メッセージの作成
        msg = MIMEText(body.encode(encoding), sub_type, encoding)
        msg['Subject'] = Header(subject, encoding)
        msg['From'] = from_addr
        msg['To'] = ', '.join(to_addrs)

        # メールサーバーへ接続して送信
        server = SMTP(smtp_server, port)
        server.starttls()
        server.login(self.mail_user, self.mail_pass)
        server.sendmail(from_addr, to_addrs, msg.as_string())
        server.quit()
