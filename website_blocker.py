import time
from datetime import datetime as dt
temphost= r"C:\Windows\System32\drivers\etc\hosts"
ip_redirect= "127.0.0.1"
websites= ["www.facebook.com", "facebook.com"]




while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("on time")
        host_content= open(temphost,"r+")
        data = host_content.read()
        for webs in websites:
            if webs in data:
                pass
            else:
                host_content.write(ip_redirect +" " +  webs+ "\n")

    else:
        with open(temphost,"r+") as host_content:
            data= host_content.readlines()
            host_content.seek(0)
            for lines in data:
                if not any(webs in lines for webs in websites):
                    host_content.write(lines)
            host_content.truncate()


        print("off time")
    time.sleep(5)