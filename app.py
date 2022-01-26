import os
from flask import Flask, request, jsonify
import schema


#Initialize
app = Flask(__name__)
my_connector = schema.MyConnector()

#All interactions traffic from Smartthings would be redirected to this method. Different handlers will diverge from here.
@app.route('/', methods=['POST']) 
def webhook():
    data = request.get_json(force=True)
    print('request:')
    print(data)
    connector_handler = my_connector.interaction_handler(data)
    print('response:')
    print(connector_handler)
    print()
    return jsonify(connector_handler)

#Any external fuzzer should reach out to this context. State call back functions are called once the command is served to
#update the state of devices in Mobile Application also.
@app.route('/fuzzer', methods=['POST'])
def fuzzer():
    data = request.get_json(force=True)
    print('request:')
    print(data)
    resObj = my_connector.update_state(data)
    return resObj

# Begin Flask Server.
if __name__ == "__main__":
    my_connector.refresh_token()
    app.run(debug=True, port=int(os.environ.get("PORT", 30001)))
