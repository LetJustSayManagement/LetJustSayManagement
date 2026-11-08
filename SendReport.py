import requests
import json
url = "https://discordapp.com/api/webhooks/1566561823551922291/_SZCo6cuU7VjVX3ZsZO5Vh32P6WyyKBJZ5kUqQTme96UWtHpw9WMhEk4kbqIrGM6hejm"

def SendReport(filename):
  with open(filename,"rb") as f:
        files = {
        "file": (filename, f, "application/json")
        }
        data={
        "content":"ASM Scan Report"
        }
        res = requests.post(url, data = data, files = files)
        print(res.status_code)
        print(res.text)




