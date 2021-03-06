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
    'Model D001')
d1_c2c_arrival_2.set_context(
    'Living',
    ['Presence Sensors'],
    ['presence-sensor'])
d1_c2c_arrival_2.set_state(
    'st.presenceSensor',
    'presence',
    'not present')
d1_c2c_arrival_2.set_state(
    'st.battery',
    'battery',
    100)
# The capability TONE has no state attributes. It has only one command -> BEEP
# d1_c2c_arrival_2.set_state(
#     'st.tone',
#     'switch',
#     'on')

#Official c2c-button-4 Device
d2_c2c_button_4 = SchemaDevice(
    'd2_c2c_button_4',
    'd2_c2c_button_4',
    'c2c-button-4',
    '002')
d2_c2c_button_4.set_mn(
    'C2C Button 4 type - Button, Holdable Button, Battery',
    'Model D002')
d2_c2c_button_4.set_context(
    'Living',
    ['Buttons'],
    ['switch'])
d2_c2c_button_4.set_state(
    'st.button',
    'button',
    'held')
#Button is holdable
d2_c2c_button_4.set_state(
    'st.battery',
    'battery',
    100)


#Official c2c-camera-2 Device
d3_c2c_camera_2 = SchemaDevice(
    'd3_c2c_camera_2',
    'd3_c2c_camera_2',
    'c2c-camera-2',
    '003')
d3_c2c_camera_2.set_mn(
    'C2C Camera 2 type - Image Capture',
    'Model D003')
d3_c2c_camera_2.set_context(
    'Living',
    ['Cameras'],
    ['camera'])
d3_c2c_camera_2.set_state(
    'st.imageCapture',
    'captureTime',
    '19700101T020000-0500')
d3_c2c_camera_2.set_state(
    'st.imageCapture',
    'encrypted',
    False)
d3_c2c_camera_2.set_state(
    'st.imageCapture',
    'image',
    'https://pixabay.com/photos/tree-sunset-clouds-sky-silhouette-736885/')


#Official c2c-carbon-monoxide-2 Device
d4_c2c_carbon_monoxide_2 = SchemaDevice(
    'd4_c2c_carbon_monoxide_2',
    'd4_c2c_carbon_monoxide_2',
    'c2c-carbon-monoxide-2',
    '004')
d4_c2c_carbon_monoxide_2.set_mn(
    'C2C Carbon Monoxide 2 type - Carbon Monoxide Detector, Battery, Tamper Alert',
    'Model D004')
d4_c2c_carbon_monoxide_2.set_context(
    'Living',
    ['Carbon Monoxide Sensors'],
    ['generic-sensor'])
d4_c2c_carbon_monoxide_2.set_state(
    'st.carbonMonoxideDetector',
    'carbonMonoxide',
    'clear')
d4_c2c_carbon_monoxide_2.set_state(
    'st.battery',
    'battery',
    100)
d4_c2c_carbon_monoxide_2.set_state(
    'st.tamperAlert',
    'tamper',
    'clear')





#Official c2c-color-temperature-bulb Device
d5_c2c_color_temperature_bulb = SchemaDevice(
    'd5_c2c_color_temperature_bulb',
    'd5_c2c_color_temperature_bulb',
    'c2c-color-temperature-bulb',
    '005')
d5_c2c_color_temperature_bulb.set_mn(
    'C2C Color Temperature Bulb type - Switch, Switch Level, Color Temperature',
    'Model D005')
d5_c2c_color_temperature_bulb.set_context(
    'Living',
    ['light'],
    ['light'])
d5_c2c_color_temperature_bulb.set_state(
    'st.switch',
    'switch',
    'on')
d5_c2c_color_temperature_bulb.set_state(
    'st.switchLevel',
    'level',
    50)
d5_c2c_color_temperature_bulb.set_state(
    'st.colorTemperature',
    'colorTemperature',
    6500)


#Official c2c-contact-2 Device
d6_c2c_contact_2 = SchemaDevice(
    'd6_c2c_contact_2',
    'd6_c2c_contact_2',
    'c2c-contact-2',
    '006')
d6_c2c_contact_2.set_mn(
    'C2C Contact 2 type - Contact Sensor, Battery, Temperature Measurement, Acceleration Sensor',
    'Model D006')
d6_c2c_contact_2.set_context(
    'Living',
    ['contact-sensor'],
    ['contact-sensor'])
d6_c2c_contact_2.set_state(
    'st.contactSensor',
    'contact',
    'closed')
d6_c2c_contact_2.set_state(
    'st.battery',
    'battery',
    50)
d6_c2c_contact_2.set_state(
    'st.temperatureMeasurement',
    'temperature',
    70,
    'C')
d6_c2c_contact_2.set_state(
    'st.accelerationSensor',
    'acceleration',
    'active')


#Official c2c-contact-4 Device
d7_c2c_contact_4 = SchemaDevice(
    'd7_c2c_contact_4',
    'd7_c2c_contact_4',
    'c2c-contact-4',
    '007')
d7_c2c_contact_4.set_mn(
    'C2C Contact 4 type - Contact Sensor, Door Control, Garage Door Control',
    'Model D007')
d7_c2c_contact_4.set_context(
    'Living',
    ['contact-sensor'],
    ['contact-sensor'])
d7_c2c_contact_4.set_state(
    'st.contactSensor',
    'contact',
    'closed')
d7_c2c_contact_4.set_state(
    'st.doorControl',               # doorControl capability has commands
    'door',
    'closed')
d7_c2c_contact_4.set_state(
    'st.garageDoorControl',               # doorControl capability has commands
    'door',
    'closed')


#Official c2c-dimmer-power-energy Device
d8_c2c_dimmer_power_energy = SchemaDevice(
    'd8_c2c_dimmer_power_energy',
    'd8_c2c_dimmer_power_energy',
    'c2c-dimmer-power-energy',
    '008')
d8_c2c_dimmer_power_energy.set_mn(
    'C2C Dimmer Power Energy type - Switch, Switch Level, Power Meter, Energy Meter',
    'Model D008')
d8_c2c_dimmer_power_energy.set_context(
    'Living',
    ['energy-meter'],
    ['energy-meter'])
d8_c2c_dimmer_power_energy.set_state(
    'st.switch',
    'switch',
    'on')
d8_c2c_dimmer_power_energy.set_state(
    'st.switchLevel',
    'level',
    50)
d8_c2c_dimmer_power_energy.set_state(
    'st.powerMeter',
    'power',
    90)
d8_c2c_dimmer_power_energy.set_state(
    'st.energyMeter',
    'energy',
    80)


#Official c2c-doorbell-2 Device
d9_c2c_doorbell_2 = SchemaDevice(
    'd9_c2c_doorbell_2',
    'd9_c2c_doorbell_2',
    'c2c-doorbell-2',
    '009')
d9_c2c_doorbell_2.set_mn(
    'C2C Doorbell 2 type - Button, Motion Sensor, Switch, Image Capture',
    'Model D009')
d9_c2c_doorbell_2.set_context(
    'Living',
    ['door-bell'],
    ['door-bell'])
d9_c2c_doorbell_2.set_state(
    'st.button',
    'button',
    'pushed')
d9_c2c_doorbell_2.set_state(
    'st.button',
    'numberOfButtons',
    500)
# d9_c2c_doorbell_2.set_state(
#     'st.button',
#     'supportedButtonValues',
#     [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])                                        # asks for array of enum, not sure what array should it be.
d9_c2c_doorbell_2.set_state(
    'st.motionSensor',
    'motion',
    'active')
d9_c2c_doorbell_2.set_state(
    'st.switch',
    'switch',
    'on')
d9_c2c_doorbell_2.set_state(                        # imageCapture has commands
    'st.imageCapture',
    'captureTime',
    '19700101T020000-0500')
d9_c2c_doorbell_2.set_state(
    'st.imageCapture',
    'encrypted',
    False)
d9_c2c_doorbell_2.set_state(
    'st.imageCapture',
    'image',
    'https://pixabay.com/photos/tree-sunset-clouds-sky-silhouette-736885/')


#Official c2c-fan-controller-4speed Device
d10_c2c_fan_controller_4speed = SchemaDevice(
    'd10_c2c_fan_controller_4speed',
    'd10_c2c_fan_controller_4speed',
    'c2c-fan-controller-4speed',
    '0010')
d10_c2c_fan_controller_4speed.set_mn(
    'C2C Fan Controller 4Speed type - Switch, Fan Speed[1,2,3,4]',
    'Model D0010')
d10_c2c_fan_controller_4speed.set_context(
    'Living',
    ['fan'],
    ['fan'])
d10_c2c_fan_controller_4speed.set_state(
    'st.switch',
    'switch',
    'on')
d10_c2c_fan_controller_4speed.set_state(
    'st.fanSpeed',
    'fanSpeed',
    6700)                                 # Fan speed has commands.


#Official c2c-humidity Device
d11_c2c_humidity = SchemaDevice(
    'd11_c2c_humidity',
    'd11_c2c_humidity',
    'c2c-humidity',
    '0011')
d11_c2c_humidity.set_mn(
    'C2C Humidity type - Relative Humidity Measurement, Battery, Temperature Measurement',
    'Model D0011')
d11_c2c_humidity.set_context(
    'Living',
    ['air-conditioner'],
    ['air-conditioner'])
d11_c2c_humidity.set_state(
    'st.relativeHumidityMeasurement',
    'humidity',
    50)
d11_c2c_humidity.set_state(
    'st.battery',
    'battery',
    50)
d11_c2c_humidity.set_state(
    'st.temperatureMeasurement',
    'temperature',
    70,
    'C')


#Official c2c-leak-3 Device
d12_c2c_leak_3 = SchemaDevice(
    'd12_c2c_leak_3',
    'd12_c2c_leak_3',
    'c2c-leak-3',
    '0012')
d12_c2c_leak_3.set_mn(
    'C2C Leak 3 type - Water Sensor, Battery, Temperature Measurement, Tamper Alert',
    'Model D0012')
d12_c2c_leak_3.set_context(
    'Living',
    ['leak-sensor'],
    ['leak-sensor'])
d12_c2c_leak_3.set_state(
    'st.waterSensor',
    'water',
    'dry')
d12_c2c_leak_3.set_state(
    'st.battery',
    'battery',
    50)
d12_c2c_leak_3.set_state(
    'st.temperatureMeasurement',
    'temperature',
    70,
    'C')
d12_c2c_leak_3.set_state(
    'st.tamperAlert',
    'tamper',
    'clear')


#Official c2c-lock-3 Device
d13_c2c_lock_3 = SchemaDevice(
    'd13_c2c_lock_3',
    'd13_c2c_lock_3',
    'c2c-lock-3',
    '0013')
d13_c2c_lock_3.set_mn(
    'C2C Lock 3 type - Lock, Battery, Temperature Measurement',
    'Model D0013')
d13_c2c_lock_3.set_context(
    'Living',
    ['smart-lock'],
    ['smart-lock'])
d13_c2c_lock_3.set_state(
    'st.lock',
    'lock',
    'unlocked')
d13_c2c_lock_3.set_state(
    'st.battery',
    'battery',
    50)
d13_c2c_lock_3.set_state(
    'st.temperatureMeasurement',
    'temperature',
    70,
    'C')


#Official c2c-motion-7 Device
d14_c2c_motion_7 = SchemaDevice(
    'd14_c2c_motion_7',
    'd14_c2c_motion_7',
    'c2c-motion-7',
    '0014')
d14_c2c_motion_7.set_mn(
    'C2C Motion 7 type - Motion Sensor, Battery, Temperature Measurement, Relative Humidity Measurement, Illuminance Measurement, Ultraviolet Index, Power Source, Tamper Alert',
    'Model D0014')
d14_c2c_motion_7.set_context(
    'Living',
    ['motion-sensor'],
    ['motion-sensor'])
d14_c2c_motion_7.set_state(
    'st.motionSensor',
    'motion',
    'active')
d14_c2c_motion_7.set_state(
    'st.battery',
    'battery',
    50)
d14_c2c_motion_7.set_state(
    'st.temperatureMeasurement',
    'temperature',
    70,
    'C')
d14_c2c_motion_7.set_state(
    'st.relativeHumidityMeasurement',
    'humidity',
    50)
d14_c2c_motion_7.set_state(
    'st.illuminanceMeasurement',
    'illuminance',
    30000)
d14_c2c_motion_7.set_state(
    'st.ultravioletIndex',
    'ultravioletIndex',
    150)
d14_c2c_motion_7.set_state(
    'st.powerSource',
    'powerSource',
    'battery')
d14_c2c_motion_7.set_state(
    'st.tamperAlert',
    'tamper',
    'clear')


#Official c2c-music-player-2 Device
d15_c2c_music_player_2 = SchemaDevice(
    'd15_c2c_music_player_2',
    'd15_c2c_music_player_2',
    'c2c-music-player-2',
    '0015')
d15_c2c_music_player_2.set_mn(
    'C2C Music Player 2 type - Music Player, Switch, Audio Notification',
    'Model D0015')
d15_c2c_music_player_2.set_context(
    'Living',
    ['network-audio'],
    ['network-audio'])
# d15_c2c_music_player_2.set_state(                   # No capability found for Music Player
#     'st.tamperAlert',
#     'tamper',
#     'clear')
d15_c2c_music_player_2.set_state(
    'st.switch',
    'switch',
    'on')
# d15_c2c_music_player_2.set_state(                      # No attributes found for Audio Notification
#     'st.audioNotification',                             # Commands found for audio notification
#     'tamper',
#     'clear')


#Official c2c-rgbw-color-bulb Device
d16_c2c_rgbw_color_bulb = SchemaDevice(
    'd16_c2c_rgbw_color_bulb',
    'd16_c2c_rgbw_color_bulb',
    'c2c-rgbw-color-bulb',
    '0016')
d16_c2c_rgbw_color_bulb.set_mn(
    'C2C RGBW Color Bulb type - Switch, Switch Level, Color Control, Color Temperature',
    'Model D0016')
d16_c2c_rgbw_color_bulb.set_context(
    'Living',
    ['light'],
    ['light'])
d16_c2c_rgbw_color_bulb.set_state(
    'st.switch',
    'switch',
    'on')
d16_c2c_rgbw_color_bulb.set_state(
    'st.switchLevel',
    'level',
    50)
# d16_c2c_rgbw_color_bulb.set_state(
#     'st.colorControl',
#     'color',
#     '{"hue":"50", "saturation":"50"}')                      # Not sure of syntax.
d16_c2c_rgbw_color_bulb.set_state(
    'st.colorControl',
    'hue',
    50)
d16_c2c_rgbw_color_bulb.set_state(
    'st.colorControl',
    'saturation',
    50)
d16_c2c_rgbw_color_bulb.set_state(
    'st.colorTemperature',
    'colorTemperature',
    15000)
















































































#Switch 1 has only switch capability
d101_switch_1 = SchemaDevice(  # Device info
    'd101_switch_1',
    'd101_switch_1',
    'c2c-switch',
    '101')
d101_switch_1.set_mn(  # Manufacturer info
    'Switch Mn Example',
    'Model X1')
d101_switch_1.set_context(
    'Living',
    ['All Lights'],
    ['switch'])
d101_switch_1.set_state(
    'st.switch',
    'switch',
    'on')
    
#Switch 2 has only switch capability
d102_switch_2 = SchemaDevice(  # Device info
    'd102_switch_2',
    'd102_switch_2',
    'c2c-switch',
    '102')
d102_switch_2.set_mn(  # Manufacturer info
    'Switch Mn Example',
    'Model X1')
d102_switch_2.set_context(
    'Living',
    ['All Lights'],
    ['switch'])
d102_switch_2.set_state(
    'st.switch',
    'switch',
    'on')

#Temp Sensor 1 can provide readings for Temperature Measurement, Contact Sensing and Battery level.
d103_temp_sensor_1 = SchemaDevice(
    'd103_temp_sensor_1',
    'd103_temp_sensor_1',
    'c2c-contact',
    '103')
d103_temp_sensor_1.set_mn(
    'Temp-Contact Sensor Manufacturer',
    'Model T1')
d103_temp_sensor_1.set_context(
    'Living',
    ['Temperature Sensors'],
    ['thermostat'])
d103_temp_sensor_1.set_state(
    'st.contactSensor',
    'contact',
    'open')
d103_temp_sensor_1.set_state(
    'st.temperatureMeasurement',
    'temperature',
    35,
    'C')
d103_temp_sensor_1.set_state(
    'st.battery',
    'battery',
    100)

#Color bulb 1 has a switch, a color control and a dimmer level setting.
d104_color_bulb_1 = SchemaDevice(
    'd104_color_bulb_1',
    'd104_color_bulb_1',
    'c2c-rgb-color-bulb',
    '104')
d104_color_bulb_1.set_mn(
    'Color Bulb Manufacturer',
    'Model C1')
d104_color_bulb_1.set_context(
    'Living',
    ['All Color Lights'],
    ['light'])
d104_color_bulb_1.set_state(
    'st.switch',
    'switch',
    'on')
d104_color_bulb_1.set_state(
    'st.switchLevel',
    'level',
    100)
# color_bulb_1.set_state(
#     'st.colorControl',
#     'color',
#     '{"hue": "75", "saturation": "65"}')
d104_color_bulb_1.set_state(
    'st.colorControl',
    'hue',
    75)
d104_color_bulb_1.set_state(
    'st.colorControl',
    'saturation',
    65)

#Fan Control 1 has a switch capability and a fanSpeed setting for controlling the speed of a virtual fan.
d105_fan_control_1 = SchemaDevice(
    'd105_fan_control_1',
    'd105_fan_control_1',
    'c2c-fan-controller-4speed',
    '105')
d105_fan_control_1.set_mn(
    'Fan Control Manufacturer',
    'Model F1')
d105_fan_control_1.set_context(
    'Living',
    ['All Fans'],
    ['fan'])
d105_fan_control_1.set_state(
    'st.switch',
    'switch',
    'on')
d105_fan_control_1.set_state(
    'st.fanSpeed',
    'fanSpeed',
    4)

#Exporting all the devices in a variable for in-memory operations
declared_devices = [d1_c2c_arrival_2, d2_c2c_button_4, d3_c2c_camera_2, d4_c2c_carbon_monoxide_2, d5_c2c_color_temperature_bulb, d6_c2c_contact_2, d7_c2c_contact_4, d8_c2c_dimmer_power_energy, d9_c2c_doorbell_2, d10_c2c_fan_controller_4speed, d11_c2c_humidity, d12_c2c_leak_3, d13_c2c_lock_3, d14_c2c_motion_7, d15_c2c_music_player_2, d16_c2c_rgbw_color_bulb, d101_switch_1, d102_switch_2, d103_temp_sensor_1, d104_color_bulb_1, d105_fan_control_1]