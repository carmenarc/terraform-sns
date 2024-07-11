import urllib3
import json

http = urllib3.PoolManager()

def lambda_handler(event, context):
    url = "http://hooks.slack.com/services/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"
    msg = {
        "channel": "#devops",
        "username": "abdessamad.ammi",
        "text": event['Records'][0]['Sns']['Message'],
        "icon_emoji": ""
    }
    
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'], 
        "status_code": resp.status, 
        "response": resp.data
    })