from stschema import SchemaDevice

light_1 = SchemaDevice(  # Device info
    'light_1',
    'light_1',
    'c2c-switch',
    '001')
light_1.set_mn(  # Manufacturer info
    'Switch Mn Example',
    'Model X1')
light_1.set_context(
    'Living',
    ['All Lights'],
    ['light'])
light_1.set_state(
    'st.switch',
    'switch',
    'on')
    
light_2 = SchemaDevice(  # Device info
    'light_2',
    'light_2',
    'c2c-color-temperature-bulb',
    '002')
light_2.set_mn(  # Manufacturer info
    'Switch Mn Example',
    'Model X1')
light_2.set_context(
    'Living',
    ['All Lights'],
    ['light'])
light_2.set_state(
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


declared_devices = [light_1, light_2, temp_sensor_1]