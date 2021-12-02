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

declared_devices = [light_1, light_2]