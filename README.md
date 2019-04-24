# amazonconnect_slack
![Amazon Connect Notification on Slack](https://i.gyazo.com/1308195568b5b505c36c2eef874ad649.png)

Amazon Connect to Slack Notification Integration

Amazon ConnectとSlack通知を連携するためのPythonで書かれたLambda用のコードです。

## 基本的な使い方
### LambdaでPythonのfunctionを作成する
このままLambdaにzipファイルをアップロードするだけで基本的には使用できます。

### Lambda上で環境変数を設定する
以下については環境変数を設定する必要があります。
 - Slackのチャンネル名
 - SlackのWebhook名

SlackのWebhookの設定については、 [https://api.slack.com/incoming-webhooks](https://api.slack.com/incoming-webhooks) をご確認ください。

## ライセンスについて
[GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl-3.0.ja.html) にて公開されています。
使用にあたっては、ライセンス規定に従って基本事項としては著作権明記は削除してはいけません。詳細は、 [https://www.gnu.org/licenses/gpl-3.0.ja.html](https://www.gnu.org/licenses/gpl-3.0.ja.html) を
御覧ください。
