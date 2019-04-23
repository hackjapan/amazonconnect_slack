import boto3
import os
import requests
import json
import urllib.request

def lambda_handler(event, context):
 SLACK_WEBHOOK = os.environ['SLACK_WEBHOOK']
 SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
 
 msg = event['Details']['Parameters']['message']

 ## Post it to Slack
# SLACK_WEBHOOK = SLACK_WEBHOOK
 payload_dic = {
    "text": "新着通話の着信中 `" + msg + "`",
    "username": "Amazon Connect",
    "channel": SLACK_CHANNEL,
 }
 r = requests.post(SLACK_WEBHOOK, data=json.dumps(payload_dic))