import requests
import threading

url = "put a website url"

requests_num = 100

def send_request():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Request sent succesfully")
    except Exception as e:
        print(e)


threads = []

for i in range(requests_num):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()