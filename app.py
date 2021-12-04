import os
from flask import Flask, request, jsonify
import schema


# Initialize
app = Flask(__name__)
my_connector = schema.MyConnector()

# forward the traffic to schema handler
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

@app.route('/fuzzer', methods=['POST'])
def fuzzer():
    data = request.get_json(force=True)
    print('request:')
    print(data)
    resObj = my_connector.update_state(data)
    return resObj

# run server
if __name__ == "__main__":
    my_connector.refresh_token()
    app.run(debug=True, port=int(os.environ.get("PORT", 30001)))
