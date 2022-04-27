from time import sleep
import requests
import json

def callStateRefresh():
    url = "https://iotpi.aplayerscreed.com/smartthings/"
    payload = {}
    with open("./stateRefreshReq.json","r") as f1:
        payload = json.load(f1)
    res = requests.post(url, json=payload)
    return res.text


def main():
    print("Beginning the constant Refresh Process!")
    while (1):
        print("Calling State Refresh Service Locally!!! (Next call in 30 seconds)")
        callStateRefresh()
        print("All OK! (Next call in 30 seconds)")
        sleep(30)   


main()