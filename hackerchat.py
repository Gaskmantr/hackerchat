import json
import threading
import random
import time,sys
import os

try:
    import requests
except:
    os.system("pip install requests")

try:
    import websocket
except:
    os.system('pip install websocket')
    os.system('pip install websocket-client')

try:
    os.system('color a')
    os.system('cls')
except:
    os.system("clear")

print("""
             __ __     __  __ __   ____  ______ 
            |  T  T   /  ]|  T  T /    T|      T
            |  l  |  /  / |  l  |Y  o  ||      |
            |  _  | /  /  |  _  ||     |l_j  l_j
            |  |  |/   \_ |  |  ||  _  |  |  |  
            |  |  |\     ||  |  ||  |  |  |  |  
            l__j__j \____jl__j__jl__j__j  l__j  
                                        -Coded by GaskmanTR-
""")

all_proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all').text
x = all_proxies.split()
b = random.choice(x)

deneme = {'http':'http://'+b}

oda = 'lexsecurity'

ws=websocket.create_connection("wss://hack.chat/chat-ws",proxies=deneme)
chars = "|/-\|"
for i in range(30):
    time.sleep(0.1)
    sys.stdout.write("\r""["+chars[i % len(chars)]+"]Connecting...")
    sys.stdout.flush()

time.sleep(0.3)
print("\n[+] Connection OK")
time.sleep(0.2)
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
    time.sleep(0.4)
