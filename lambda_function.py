import boto3
import os
import requests
import json
import urllib.request

def lambda_handler(event, context):
 SLACK_WEBHOOK = os.environ['SLACK_WEBHOOK']
 SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
 AMAZON_URL = os.environ['AMAZON_URL']
 
 tel_number_int = event['Details']['ContactData']['CustomerEndpoint']['Address']
 
 if '+81' in tel_number_int:
  tel_number_jp = tel_number_int[3:]
  tel_number_digit = len(tel_number_jp)
 else:
  tel_number_local = tel_number_int
  tel_number_digit = 0

 if '+81' in tel_number_int and tel_number_digit == 10:
  tel_number_local = '0' + tel_number_jp[0:2] + '-' + tel_number_jp[2:6] + '-' + tel_number_jp[6:10]
 elif '+81' in tel_number_int and tel_number_digit == 9:
  tel_number_local = '0' + tel_number_jp[0] + '-' + tel_number_jp[1:5] + '-' + tel_number_jp[5:9]
 else:
  tel_number_local = tel_number_int


 ## Post it to Slack
 
 slack_push = {
 "username": "Amazon Connect",
 "channel": SLACK_CHANNEL,
 "text": "通話の着信中 `" + tel_number_local  + "`",
	"attachments": [
	 {
   "fallback": "電話の着信に対応する",
   "actions": [
    {
     "type": "button",
     "text": "Amazon Connectで受話",
     "url": AMAZON_URL
    }
    ]
  }
  ]
 }
 
 request = requests.post(SLACK_WEBHOOK, data=json.dumps(slack_push))
