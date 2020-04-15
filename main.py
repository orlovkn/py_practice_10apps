import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com", "vk.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        print("Working hours...")
    else:
        print("Fun hours...")
    time.sleep(5)