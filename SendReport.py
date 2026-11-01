import requests
import json
url = "https://discord.com/api/webhooks/1566561823551922291/_SZCo6cuU7VjVX3ZsZO5Vh32P6WyyKBJZ5kUqQTme96UWtHpw9WMhEk4kbqIrGM6hejm"

def SendReport():
  with open(filename,"") as file:
      report =json.load(file)
  message = json.dumps(report, indednt = 2)
  
  payload = "content" : f"{message}"
  
  res = requests.post(url,json =payload)
  print(response.status_code)
