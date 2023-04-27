#!/usr/bin/env python3

import sys
import time
import requests

TOKEN = sys.argv[1]
URL = "http://rid.ck.ua/api/v1/words/{}.json?auth_token={TOKEN}"

for i in range(20_000, 30_000):
    url = URL.format(i)
    response = requests.get(url)

    if response.status_code == 200:
        with open(f"words/{i:05d}.json", "w") as file:
            file.write(response.text)
        print(f"{i}: {response.json()['title']}")
    else:
        print(f"{i}: {response.status_code} {response.text}")
