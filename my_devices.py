from stschema import SchemaDevice

# external_device_id=None,
# friendly_name=None,
# device_handler_type=None,
# device_unique_id=None,
# device_cookie=None,
# REFER TO :- https://developer-preview.smartthings.com/docs/devices/cloud-connected/device-handler-types
# REFER TO :- https://developer-preview.smartthings.com/docs/devices/capabilities/capabilities-reference/

# room_name, groups, categories
# REFER TO :- https://developer-preview.smartthings.com/docs/devices/device-profiles [CATEGORIES]

# def set_state(self, capability, attribute, value, unit=None, component="main")
# SET STATE : REFER TO :- https://developer-preview.smartthings.com/docs/devices/capabilities/capabilities-reference/


#Official c2c-arrival-2 Device
d1_c2c_arrival_2 = SchemaDevice(
    'd1_c2c_arrival_2',
    'd1_c2c_arrival_2',
    'c2c-arrival-2',
    '001')
d1_c2c_arrival_2.set_mn(
    'C2C Arrival 2 type - Presence, Battery, Tone',
    'Model X1')
d1_c2c_arrival_2.set_context(
    'Living',
    ['Presence'],
    ['presence-sensor'])
d1_c2c_arrival_2.set_state(
    'st.presenceSensor',
    'presence',
    'present')
d1_c2c_arrival_2.set_state(
    'st.battery',
    'battery',
    100)
# The capability TONE has no state attributes. It has only one command -> BEEP
# d1_c2c_arrival_2.set_state(
#     'st.tone',
#     'switch',
#     'on')

#Switch 1 has only switch capability
switch_1 = SchemaDevice(  # Device info
    'switch_1',
    'switch_1',
    'c2c-switch',
    '101')
switch_1.set_mn(  # Manufacturer info
    'Switch Mn Example',
    'Model X1')
switch_1.set_context(
    'Living',
    ['All Lights'],
    ['switch'])
switch_1.set_state(
    'st.switch',
    'switch',
    'on')
    
#Switch 2 has only switch capability
switch_2 = SchemaDevice(  # Device info
    'switch_2',
    'switch_2',
    'c2c-switch',
    '102')
switch_2.set_mn(  # Manufacturer info
    'Switch Mn Example',
    'Model X1')
switch_2.set_context(
    'Living',
    ['All Lights'],
    ['switch'])
switch_2.set_state(
    'st.switch',
    'switch',
    'on')

#Temp Sensor 1 can provide readings for Temperature Measurement, Contact Sensing and Battery level.
temp_sensor_1 = SchemaDevice(
    'temp_sensor_1',
    'temp_sensor_1',
    'c2c-contact',
    '103')
temp_sensor_1.set_mn(
    'Temp-Contact Sensor Manufacturer',
    'Model T1')
temp_sensor_1.set_context(
    'Living',
    ['Temperature Sensors'],
    ['thermostat'])
temp_sensor_1.set_state(
    'st.contactSensor',
    'contact',
    'open')
temp_sensor_1.set_state(
    'st.temperatureMeasurement',
    'temperature',
    35,
    'C')
temp_sensor_1.set_state(
    'st.battery',
    'battery',
    100)

#Color bulb 1 has a switch, a color control and a dimmer level setting.
color_bulb_1 = SchemaDevice(
    'color_bulb_1',
    'color_bulb_1',
    'c2c-rgb-color-bulb',
    '104')
color_bulb_1.set_mn(
    'Color Bulb Manufacturer',
    'Model C1')
color_bulb_1.set_context(
    'Living',
    ['All Color Lights'],
    ['light'])
color_bulb_1.set_state(
    'st.switch',
    'switch',
    'on')
color_bulb_1.set_state(
    'st.switchLevel',
    'level',
    100)
# color_bulb_1.set_state(
#     'st.colorControl',
#     'color',
#     '{"hue": "75", "saturation": "65"}')
color_bulb_1.set_state(
    'st.colorControl',
    'hue',
    75)
color_bulb_1.set_state(
    'st.colorControl',
    'saturation',
    65)

#Fan Control 1 has a switch capability and a fanSpeed setting for controlling the speed of a virtual fan.
fan_control_1 = SchemaDevice(
    'fan_control_1',
    'fan_control_1',
    'c2c-fan-controller-4speed',
    '105')
fan_control_1.set_mn(
    'Fan Control Manufacturer',
    'Model F1')
fan_control_1.set_context(
    'Living',
    ['All Fans'],
    ['fan'])
fan_control_1.set_state(
    'st.switch',
    'switch',
    'on')
fan_control_1.set_state(
    'st.fanSpeed',
    'fanSpeed',
    4)

#Exporting all the devices in a variable for in-memory operations
declared_devices = [d1_c2c_arrival_2, switch_1, switch_2, temp_sensor_1, color_bulb_1, fan_control_1]