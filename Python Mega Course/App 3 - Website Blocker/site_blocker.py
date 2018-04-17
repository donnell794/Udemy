import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

sleep_time = 5
start_hour = 8
start_time = dt(dt.now().year,dt.now().month,dt.now().day,start_hour)
end_hour = 16
end_time = dt(dt.now().year,dt.now().month,dt.now().day,end_hour)
while True:
    if start_time < dt.now() < end_time:
        #print("Working Hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "\t" + website + "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        #print("Fun Hours...")
    time.sleep(sleep_time)
