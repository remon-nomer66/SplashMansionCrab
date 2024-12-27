# send_sms.py

import logging

class SMSNotification:
    def __init__(self, recipients=None):
        """
        SMS通知クラス
        :param recipients: 受信者リスト
        """
        self.recipients = recipients if recipients else []

    def set_recipients(self, recipients):
        """
        受信者リストを設定する
        """
        self.recipients = recipients

    def send_notification(self, message):
        """
        SMSを送信する処理
        :param message: 送信するメッセージ内容
        """
        for recipient in self.recipients:
            # 実際のSMS送信処理をここに記述
            # 例: 外部APIを呼び出してSMSを送信
            # response = sms_api.send(to=recipient, message=message)
            logging.info(f"SMS送信先: {recipient}, メッセージ: {message}")
            # ダミー送信としてログに記録
            pass