#Code By AKANINE
#Discord Hook-Say

import requests
from requests import post
import random
import threading
from fake_useragent import UserAgent

ua = UserAgent()
a = ua.random
user_agent = ua.random

useragent = user_agent



Hook = input("Hook >")
msg = input("Mss >")
flood = int(input("flood >"))

data = {
          "content": f"{msg}",
          "username": f"NINEิ",
          "avatar_url": f"https://cdn.discordapp.com/attachments/989156872655372318/989486923645087754/Captur232323233e.PNG",
          "tts": True
        }
    


def floodv1():
    requests.post(Hook, headers={"User-Agent": useragent}, json=data)
    



for aka in range(flood):
        th = threading.Thread(target = floodv1)
        th.start()