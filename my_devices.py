from stschema import SchemaDevice

switch_1 = SchemaDevice(  # Device info
    'switch_1',
    'switch_1',
    'c2c-switch',
    '001')
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
    
switch_2 = SchemaDevice(  # Device info
    'switch_2',
    'switch_2',
    'c2c-switch',
    '002')
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

temp_sensor_1 = SchemaDevice(
    'temp_sensor_1',
    'temp_sensor_1',
    'c2c-contact',
    '003')
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

color_bulb_1 = SchemaDevice(
    'color_bulb_1',
    'color_bulb_1',
    'c2c-rgb-color-bulb',
    '004')
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

fan_control_1 = SchemaDevice(
    'fan_control_1',
    'fan_control_1',
    'c2c-fan-controller-4speed',
    '005')
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

declared_devices = [switch_1, switch_2, temp_sensor_1, color_bulb_1, fan_control_1]