import onionGpio
import sys
import time
from OmegaExpansion import relayExp


def changeSwitch(pin, value):
	light = onionGpio.OnionGpio(pin)
	light.setOutputDirection(0)
	if value == 0:
		light.setValue(1)
	else:
		light.setValue(0)
	return


def setRelay(address, channel, value):
	print 'started'
	# address = int(address)
	if address < 0 or address > 7:
		return
	print 'Starting to use relay-exp functions on addr offset', address
	relayExp.setVerbosity(0)
	if relayExp.checkInit(address) == 0:
		ret = relayExp.driverInit(address)
		time.sleep(1)
	if channel == 0 or channel == 1:
		result = relayExp.setChannel(address, channel, value)
		time.sleep(2)
	else:
		print 'El relay esta mal configurado en el servidor, debe ser 0 o 1'
	final_value = relayExp.readChannel(address, channel)
	if final_value != value:
		print 'Hubo un error, el valor final no coincide'
	return


def setIntensity(value):
	file = open('intensity.txt', 'w')
	file.write(str(value))
	file.close()
	print 'se modifico el archivo.. valor: ', value
	return


eval(sys.argv[1])

