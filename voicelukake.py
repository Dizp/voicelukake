from colorama import Fore
import requests
from datetime import datetime
import random
import threading
from pystyle import Colors, Colorate
import json
import time

token = input(f"Token: ")
ID = int(input(f"ID: "))




regions = [
    'brazil',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]


def Nicedayzzz():
    headers = {
        "accept": "*/*",
        "accept-language": "th-TH,th;q=0.9",
        "authorization": token,
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "th",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRoLVRIIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMzMTQyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }

    group = f"https://discord.com/api/v9/channels/{int(ID)}"
    RandomRegion = random.choice(regions)
    payload = {"type": 2, "topic": "", "bitrate": 64000, "user_limit": 0, "nsfw": False, "flags": 0,"rate_limit_per_user": 0, "rtc_region": RandomRegion, "default_reaction_emoji": None}
    try:
        r = requests.patch(group, json=payload,headers=headers)
        s = [200, 201, 204]
        if r.status_code in s:
            print(f"down {r.status_code}")
        elif r.status_code == 429:
            b = r.json()
            print(F"retry_after {b['retry_after']}")
            time.sleep(b['retry_after'])
    except:
        pass


def Nicedayz1():
    for i in range(10000000000000000000000000):
        t = threading.Thread(target=Nicedayzzz)
        t.start()
Nicedayz1()
