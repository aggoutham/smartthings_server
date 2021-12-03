import requests
from uuid import uuid4
from stschema import SchemaConnector, SchemaDevice
from stschema.schema_response.responses import StateResponse, StateRefreshResponseSchema
from stschema.util.base_modules.base_response import BaseResponse
from apscheduler.schedulers.background import BackgroundScheduler
from stschema.util.base_modules import BaseState
import my_devices

# Credentials_For_Yilu's_Project
# client_id = ""
# client_secret = ""

# Credentials_For_Goutham's_Project
client_id = ""
client_secret = ""

my_active_devices = my_devices.declared_devices

# scheduler init
scheduler = BackgroundScheduler()

# MyConnector definition
class MyConnector(SchemaConnector):
    def __init__(self, *opts):
        SchemaConnector.__init__(self, enable_logger=True)

    def discovery_handler(self, request_id, access_token):
        # Device definition using the SchemaDevice class
        
        my_active_devices = my_devices.declared_devices
        return self.discovery_response(my_active_devices, request_id)

    def state_refresh_handler(self, devices, request_id, access_token):
        # Collection of devices
        filtered_devices = []
        # State Refresh Request information
        for device in devices:
            for my_d in my_active_devices:
                if device['externalDeviceId'] == my_d.external_device_id: 
                    filtered_devices.append(my_d)
        return self.state_refresh_response(filtered_devices, request_id)

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
                        for stateObj in existing_states:
                            if stateObj.capability == capability:
                                updatedStateObj = self.handleIndividualCommands(stateObj,command,component,capability,arguments)
                                my_device.states.append(updatedStateObj)
                            else:
                                my_device.states.append(stateObj)
                        filteredDevices.append(my_device)
        return self.command_response(filteredDevices, request_id)

    def interaction_result_handler(self, interaction_result: dict, origin: str):
        print(interaction_result, origin)
        pass

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
        # schedule token refresh
        scheduler.add_job(self.refresh_token, 'interval', seconds=self.callback_authentication['expiresIn'])
        # scheduler.add_job(self.refresh_token, 'interval', seconds=60)
        scheduler.start()
        return

    def refresh_token(self):
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
        res = requests.post(self.callback_urls['oauthToken'], json=token_request)
        print('request access token:')
        print(token_request)
        print('response from server:')
        print(res.text)
        self.callback_authentication = res.json()['callbackAuthentication']
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
        print('response from server:')
        print(res.text)
        return
    
    # change device state
    def update_state(self):
        # my_devices.my_switch.states[0].value = command
        self.state_callback_handler()
        return

    # Behaviours for each command
    def handleIndividualCommands(self, oldStateObj,command,component,capability,arguments):
        newStateObj = oldStateObj
        if "st.switch" in capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='switch',
                value=command,
                unit=None,
                component="main"
            )
        elif "st.contactSensor" in capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='contact',
                value=command,
                unit=None,
                component="main"
            )
        elif "st.temperatureMeasurement" in capability:
            newStateObj = BaseState(
                capability=capability,
                attribute='temperature',
                value=command,
                unit="C",
                component="main"
            )
        return newStateObj

    