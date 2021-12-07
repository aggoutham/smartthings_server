Steps to instantiate the environment :- 

1. Create a schema connector in Samsung Developer Workspace - "https://smartthings.developer.samsung.com/workspace/projects". 

2. During the set up, enter correct webhook URL in the workspace project. Eg :- "https://iotpi.aplayerscreed.com/smartthings/" is where our Raspberry Pi (Port 30001) is hosted. Enter mocking OAuth server details to fake OAuth flow -

Client Id: dummy-client-id
client Secret: dummy-client-secret
Auth URI : https://mock-oauth2-server.glitch.me/o/oauth2/v2/auth
Token URI: https://mock-oauth2-server.glitch.me/oauth2/v4/token

3. Once the setup is completed, Samsung Smartthings will provide a secret "client_id" and "client_secret" for authentication purposes. Enter this information in "schema.py" script.

4. Start the flask server by running this command - "python3 app.py"

5. Go to Samsung Smartthings Mobile application (Andriod/iOS) and log in using the same user as Developer Workspace. Enable Developer Mode in Samsung Smartthings mobile app. Refer - https://developer-preview.smartthings.com/docs/devices/test-your-device/

6. Go to "Add Device" and scroll down till you find "My Testing Device". Click on the icon and identify your project name in this window. Click on the project name.

7. There will be a redirect to Oauth servers and upon clicking on "Authorize" button the connection between Samsung Smartthings and the Flask server will be successful. 

8. After these steps, we can find 5 devices successfully set up in the Living Room View.


Steps to run fuzzing on the virtual devices :-

1. Once the environment is set-up, run the "fuzzer/fuzzer.py" script. Different test cases for different capabilities will continue to run one-by-one.

2. Check all the client/server related logs within the "fuzzer.log" file.
