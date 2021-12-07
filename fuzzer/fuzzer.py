import requests, sys
from uuid import uuid4
from random import randint, uniform

fuzzing_url = "https://iotpi.aplayerscreed.com/vdev_py/fuzzer"

reqObj = {}
reqObj["headers"] = {}
reqObj["headers"]["requestId"] = str(uuid4())
reqObj["devices"] = []
reqObj["devices"].append({})
reqObj["devices"][0]["externalDeviceId"] = ""
reqObj["devices"][0]["commands"] = []

sampleCommandObj = {}
sampleCommandObj["component"] = "main"
sampleCommandObj["capability"] = ""
sampleCommandObj["command"] = ""
sampleCommandObj["arguments"] = []

### Sending requesto to Flask App
def hiturl(payload):
    res = requests.post(fuzzing_url, json=payload)
    print('response from server:')
    print(res.text)
    return res.text

#### Loop through different test cases for different capabilities
def main():
    print("Starting Fuzzer...")

    # fan_control_1
    # set fanspeed
    # Fuzz fanSpeed Capability
    req = dict(reqObj)
    req["devices"][0]["externalDeviceId"] = "fan_control_1"
    commandObj = dict(sampleCommandObj)
    commandObj["capability"] = "st.fanSpeed"
    commandObj["command"] = "setFanSpeed"
    num = sys.maxsize + 1
    commandObj["arguments"] = [num]
    print(num)
    req["devices"][0]["commands"].append(commandObj)
    res = hiturl(req)
    # loop call
    for i in range(1, 100):
        req["devices"][0]["commands"][0]["arguments"] = [i]
        res = hiturl(req)

    # temp_sensor_1
    # st.contactSensor
    # Fuzz contact sensor capability
    req = dict(reqObj)
    req["devices"][0]["externalDeviceId"] = "temp_sensor_1"
    commandObj = dict(sampleCommandObj)
    commandObj["capability"] = "st.contactSensor"
    commandObj["command"] = "open"
    commandObj["arguments"] = []
    req["devices"][0]["commands"].append(commandObj)
    res = hiturl(req)
    # loop call
    for i in range(1, 100):
        randStr = random_string(10)
        print(randStr)
        req["devices"][0]["commands"][0]["command"] = randStr
        res = hiturl(req)
    
    # st.temperatureMeasurement
    # Fuzz temperature sensor capability
    req = dict(reqObj)
    req["devices"][0]["externalDeviceId"] = "temp_sensor_1"
    commandObj = dict(sampleCommandObj)
    commandObj["capability"] = "st.temperatureMeasurement"
    commandObj["command"] = 0
    commandObj["arguments"] = []
    req["devices"][0]["commands"].append(commandObj)
    res = hiturl(req)
    # loop call
    for i in range(1, 100):
        req["devices"][0]["commands"][0]["command"] = randint(-460, 10000)
        res = hiturl(req)

    # st.battery
    # Fuzz battery level capability
    req = dict(reqObj)
    req["devices"][0]["externalDeviceId"] = "temp_sensor_1"
    commandObj = dict(sampleCommandObj)
    commandObj["capability"] = "st.battery"
    commandObj["command"] = 0
    commandObj["arguments"] = []
    req["devices"][0]["commands"].append(commandObj)
    res = hiturl(req)
    # loop call
    for i in range(1, 100):
        req["devices"][0]["commands"][0]["command"] = randint(-100, 200)
        res = hiturl(req)

    # switch_1
    # st.switch
    # Fuzz switch capability
    req = dict(reqObj)
    req["devices"][0]["externalDeviceId"] = "switch_1"
    commandObj = dict(sampleCommandObj)
    commandObj["capability"] = "st.switch"
    commandObj["command"] = "on"
    commandObj["arguments"] = []
    req["devices"][0]["commands"].append(commandObj)
    res = hiturl(req)
    # loop call
    for i in range(1, 100):
        randStr = random_string(10)
        print(randStr)
        req["devices"][0]["commands"][0]["command"] = randStr
        res = hiturl(req)

    # color_bulb_1
    # st.switchLevel
    # Fuzz dimmer level capability
    req = dict(reqObj)
    req["devices"][0]["externalDeviceId"] = "color_bulb_1"
    commandObj = dict(sampleCommandObj)
    commandObj["capability"] = "st.switchLevel"
    commandObj["command"] = 0
    commandObj["arguments"] = [0]
    req["devices"][0]["commands"].append(commandObj)
    res = hiturl(req)
    # loop call
    for i in range(1, 101):
        req["devices"][0]["commands"][0]["arguments"][0] = i
        res = hiturl(req)

    # st.colorControl
    # Fuzz color control capability by setting hue and saturation individually
    req = dict(reqObj)
    req["devices"][0]["externalDeviceId"] = "color_bulb_1"
    commandObj = dict(sampleCommandObj)
    commandObj["capability"] = "st.colorControl"
    commandObj["command"] = "setHue"
    commandObj["arguments"] = [0]
    req["devices"][0]["commands"].append(commandObj)
    res = hiturl(req)
    req["devices"][0]["commands"][0]["command"] = "setSaturation"
    res = hiturl(req)
    # loop call
    for i in range(1, 100):
        req["devices"][0]["commands"][0]["command"] = "setHue"
        req["devices"][0]["commands"][0]["arguments"][0] = randint(0, 100)
        res = hiturl(req)
        req["devices"][0]["commands"][0]["command"] = "setSaturation"
        req["devices"][0]["commands"][0]["arguments"][0] = randint(0, 100)
        res = hiturl(req)

# Generate random ASCII string
def random_string(length): 
    randStr = ""
    for i in range(length):
        randStr = randStr + chr(randint(0, 127))
        # print(randStr)
    return randStr

main()