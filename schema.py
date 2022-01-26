import requests, json, logging
from uuid import uuid4
from stschema import SchemaConnector, SchemaDevice
from stschema.schema_response.responses import StateResponse, StateRefreshResponseSchema
from stschema.util.base_modules.base_response import BaseResponse
from apscheduler.schedulers.background import BackgroundScheduler
from stschema.util.base_modules import BaseState
import my_devices

# Credentials_For_Yilu's_Project
# client_id = "651cadcf-4966-48ae-819c-fc5341e3c0ea"
# client_secret = "ff5db68d952cf89448a9f2248fee65029e040ac6dc28dbf447f341edd5f94f609861ded5d9567c4b3a5d44c8591ea47338d09be27a14926bdefa194cc18a8ee121e9ecfd54546eacb018487e8a157254adf39b753bb228092c53a446995e064cf451e90afeb9901b90ecf60a36c47d0c8af52cff001e8742c97b9b60744dee1632838da0c18a02ed41ddbdc314ec5f4ae0456a70e0989806c200a44186077d6c6c076535bd1aeda7e946b89da184b2a7bee0314344787c7c86467f6221b05fe7291fafc5a3064beffd32b4ab3a4315a7babc3551d8077cc9dfc209e2b974971e90b83c5d937bf2ec131ae696b3084109bd99d4813427a4a534c18b0b900d503e"

# Credentials_For_Goutham's_Project
client_id = "e64bfbe4-09bf-4deb-b741-8713e0b12d0d"
client_secret = "7ec4a30ea8133c4ee07853c632e68e7c0e479839cb24083af9b7333256a53e33fe0b0a961b4abc5308374feedd58798537da207f75ec2365aa49d49d4f03412dc752c974b430c636d3e70d6218b5f56eaba317f9b419b5af31189511c6895a1037f2e4dc6b78b73702a5dfbddbf968c7a3e8939751bfebbdd0f53303f4eff5c60d33873a74e46255ac091d7dad2d710e0e7800c019174a1aef5605cc3c5a6300a245d648cf7c581525a38096bca7bf192d79c0bf1011becf5ce2d3122020ed3d6210cf2346dd91960a7d5d0dfc702434c743d54dfdf63bfaffffd457b52f92f2bfe61fb6327297c822849839fbe85ed3c3be97f0d9aaf98fb62393214bea85ef"

my_active_devices = my_devices.declared_devices
placeholder = "initial"
logging.basicConfig(filename='fuzzer.log', level=logging.CRITICAL)
logging.critical('Server starts')

# scheduler init
scheduler = BackgroundScheduler()

# MyConnector definition
class MyConnector(SchemaConnector):
    def __init__(self, *opts):
        SchemaConnector.__init__(self, enable_logger=True)

    #Initial Discover Request Handler for Smartthings
    def discovery_handler(self, request_id, access_token):
        my_active_devices = my_devices.declared_devices
        return self.discovery_response(my_active_devices, request_id)

    #Returns latest state of all devices from in-app memory
    def state_refresh_handler(self, devices, request_id, access_token):
        # Collection of devices
        filtered_devices = []
        # State Refresh Request information
        for device in devices:
            for my_d in my_active_devices:
                if device['externalDeviceId'] == my_d.external_device_id: 
                    filtered_devices.append(my_d)
        return self.state_refresh_response(filtered_devices, request_id)

    #Filters commands individually from the request and uses handleIndividualCommands method to cater to them
    def command_handler(self, devices, request_id, access_token):
        filteredDevices = []
        for reqObj in devices:
            device_id = reqObj['externalDeviceId']
            commands = reqObj['commands']
            for commandObj in commands:
                command = commandObj['command']
                component = commandObj['component']
                capability = commandObj['capability']
                arguments = commandObj['arguments']
                for my_device in my_active_devices:
                    if device_id == my_device.external_device_id:
                        existing_states = list(my_device.states)
                        my_device.states = []
                        check = 0
                        for stateObj in existing_states:
                            if stateObj.capability == capability:
                                check = 1
                                updatedStateObj = self.handleIndividualCommands(stateObj,command,component,capability,arguments)
                                my_device.states.append(updatedStateObj)
                            else:
                                my_device.states.append(stateObj)
                        if check == 0:
                            updatedStateObj = self.handleIndividualCommands(stateObj,command,component,capability,arguments)
                            my_device.states.append(updatedStateObj)
                        filteredDevices.append(my_device)
        return self.command_response(filteredDevices, request_id)

    #To Do. All other interactions
    def interaction_result_handler(self, interaction_result: dict, origin: str):
        print(interaction_result, origin)
        pass

    #Get access token after oauth callback
    def grant_callback_access(self, callback_authentication: dict, callback_urls):
        self.callback_urls = callback_urls
        # access token request
        token_request = {
            "headers": {
                "schema": "st-schema",
                "version": "1.0",
                "interactionType": "accessTokenRequest",
                "requestId": str(uuid4())
            },
            "callbackAuthentication": {
                "grantType": "authorization_code",
                "code": callback_authentication['code'],
                "clientId": client_id,
                "clientSecret": client_secret
            }
        }
        res = requests.post(callback_urls['oauthToken'], json=token_request)
        print('request access token:')
        print(token_request)
        print('response from server:')
        print(res.text)
        self.callback_authentication = res.json()['callbackAuthentication']
        # save the token information in a file
        with open("/home/pi/accessToken.json","w") as f1:
            f1.write(json.dumps(self.callback_authentication))
        with open("/home/pi/callbackUrls.json","w") as f2:
            f2.write(json.dumps(self.callback_urls))
        # schedule token refresh
        global placeholder
        placeholder = "callback"
        # scheduler.add_job(self.refresh_token, 'interval', seconds=self.callback_authentication['expiresIn'])
        scheduler.add_job(self.refresh_token, 'interval', seconds=900)
        scheduler.start()
        return

    #Refresh access token regularly
    def refresh_token(self):
        if placeholder == "initial":
            #read refersh token from file
            try:
                with open("/home/pi/accessToken.json","r") as f1:
                    fileText = json.load(f1)
                    self.callback_authentication = fileText
            except Exception as e:
                print(e)
                print("Access Token file not present in /home/pi/")
                return
            # read callback urls file
            try:
                with open("/home/pi/callbackUrls.json","r") as f2:
                    fileText = json.load(f2)
                    self.callback_urls = fileText
            except Exception as e:
                print(e)
                print("Callback Urls file not present in /home/pi/")
                return
        elif placeholder == "callback":
            pass

        # access token request
        token_request = {
            "headers": {
                "schema": "st-schema",
                "version": "1.0",
                "interactionType": "refreshAccessTokens",
                "requestId": str(uuid4())
            },
            "callbackAuthentication": {
                "grantType": "refresh_token",
                "refreshToken": self.callback_authentication['refreshToken'],
                "clientId": client_id,
                "clientSecret": client_secret
            }
        }
        res = requests.post(self.callback_urls["oauthToken"], json=token_request)
        print('request access token:')
        print(token_request)
        print('response from server:')
        print(res.text)
        self.callback_authentication = res.json()['callbackAuthentication']
        # save the token information in a file
        with open("/home/pi/accessToken.json","w") as f1:
            f1.write(json.dumps(self.callback_authentication))
        with open("/home/pi/callbackUrls.json","w") as f2:
            f2.write(json.dumps(self.callback_urls))
        return

    # send device state to server
    def state_callback_handler(self):
        response = StateResponse(
            devices = my_active_devices,
            interaction_type = 'stateCallback',
            request_id = str(uuid4())               
        )
        response.authentication = {
                "tokenType": "Bearer",
                "token": self.callback_authentication['accessToken']
            }
        state_schema = StateRefreshResponseSchema()
        states = state_schema.dump(response)
        res = requests.post(self.callback_urls['stateCallback'], json=states)
        print('state callback:')
        print(states)
        print(self.callback_urls['stateCallback'])
        logging.critical('state callback:')
        logging.critical(states)
        print('response from server:')
        print(res.text)
        logging.critical('response from server:')
        logging.critical(res.text)
        return res.text
    
    # change device state
    def update_state(self,reqObj):
        request_id = reqObj["headers"]["requestId"]
        if "devices" in reqObj:
            devices = reqObj["devices"]
            resObj = self.command_handler(devices,request_id,self.callback_authentication['accessToken'])
        resText = self.state_callback_handler()
        return resText

    # Behaviours for each command
    def handleIndividualCommands(self, oldStateObj,command,component,capability,arguments):
        newStateObj = oldStateObj
        if "st.switch" == capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='switch',
                value=command,
                unit=None,
                component="main"
            )
        elif "st.contactSensor" == capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='contact',
                value=command,
                unit=None,
                component="main"
            )
        elif "st.temperatureMeasurement" == capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='temperature',
                value=command,
                unit="C",
                component="main"
            )
        elif "st.battery" == capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='battery',
                value=command,
                unit="%",
                component="main"
            )
        elif "st.switchLevel" == capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='level',
                value=arguments[0],
                unit=None,
                component="main"
            )
        elif "st.colorControl" == capability:
            if command == "setColor":
                attribute = "color"
                if oldStateObj.attribute != "color":
                    return oldStateObj
                value = str(arguments[0])
            elif command == "setHue":
                attribute = "hue"
                if oldStateObj.attribute != "hue":
                    return oldStateObj
                value = (arguments[0])
            elif command == "setSaturation":
                attribute = "saturation"
                if oldStateObj.attribute != "saturation":
                    return oldStateObj
                value = (arguments[0])
            newStateObj = BaseState(
                capability=capability,
                attribute=attribute,
                value=value,
                unit=None,
                component="main"
            )
        elif "st.fanSpeed" == capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='fanSpeed',
                value=arguments[0],
                unit=None,
                component="main"
            )
        return newStateObj

    