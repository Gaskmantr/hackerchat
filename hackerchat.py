import json
import websocket
import threading
import random
import requests
import time
import os

os.system('cls')

all_proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all').text
x = all_proxies.split()
b = random.choice(x)

deneme = {'http':'http://'+b}

oda = input("Enter room ID:")

ws=websocket.create_connection("wss://hack.chat/chat-ws",proxies=deneme)
print("[+] Connection OK")

nick=input("Enter Nickname: ")
ws.send(json.dumps({"cmd":"join","channel":"{}".format(oda),"nick":nick}))

def onliness(wait):
	time.sleep(wait)
	onlines=json.loads(ws.recv())["nicks"]
	print("Online Users: "+', '.join(onlines))
onliness(0)

def recvThread():
    while 1:
        data=json.loads(ws.recv())
        if(data["cmd"]=="chat"):
            if(data["nick"]!=nick):
                print("\n"+data["nick"]+":"+data["text"])
        print("\r{}:".format(nick)+str(),end="")
threading.Thread(target=recvThread).start()

while 1:
    print("\r{}:".format(nick)+str(),end="")
    data=input("")
    data={"cmd":"chat","text":"\n"+data+"\n"}
    ws.send(json.dumps(data))
    time.sleep(0.3)
