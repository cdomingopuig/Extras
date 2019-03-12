import os
import json
import oneWire
import temperatureSensor
import oledHelper
import urllib3

# import config
dirName = os.path.dirname(os.path.abspath(__file__))
# read the config file relative to the script location
with open( '/'.join([dirName, 'config.json']) ) as f:
    config = json.load(f)

onionID = config["onionID"]
direction = config["url"]
oneWireGpio = 19

def __main__():
    # initialize oled
    # oledHelper.init(dirName)

    if not oneWire.setupOneWire(str(oneWireGpio)):
        print "Kernel module could not be inserted. Please reboot and try again."
        return -1

    # get the address of the temperature sensor
    # 	it should be the only device connected in this experiment    
    sensorAddress = oneWire.scanOneAddress()

    # instantiate the temperature sensor object
    sensor = temperatureSensor.TemperatureSensor("oneWire", { "address": sensorAddress, "gpio": oneWireGpio })
    if not sensor.ready:
        print "Sensor was not set up correctly. Please make sure that your sensor is firmly connected to the GPIO specified above and try again."
        return -1

    # check and print the temperature
    temperature = int(sensor.readValue())
    dataPoint = {
        "temperature": temperature
    }
    
    try:
	    data = { 'intermediary' : onionID, 'value': temperature}
	    encoded_data = json.dumps(data).encode('utf-8')
	    http = urllib3.PoolManager()
	    url = 'http://' + direction + '/setTemperature'
	    print("sending updated temperature to server")
	    print(temperature)
	    r = http.request('PUT', url, body=encoded_data, headers={'Content-Type': 'application/json'})
    except ValueError:
    	print("- - - - - - - - - - - - ERROR - - - - - - - - - - - - - -")
    	print(ValueError)
    print("- - - - - - - - - - - - DONE - - - - - - - - - - - - - -")
    print(r).argv[1]

	
    # write to oled screen
    # oledHelper.writeMeasurements(temperature)
    
if __name__ == '__main__':
    __main__()