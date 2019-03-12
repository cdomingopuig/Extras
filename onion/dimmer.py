import onionGpio
import sys

def dimmer(percentage):
	if int(percentage) < 10:
		return
	pins = [11, 3, 2, 18, 19, , 0, 1]
	value = int(int(percentage)*1.28)
	
	output = bin(value)[2:].zfill(8)
	print output
	for i in range(0, 8):
		pinI = onionGpio.OnionGpio(int(pins[i]))
		pinI.setOutputDirection()
		pinI.setValue(int(output[i]))
		print output[i], ' - ', pins[i]
		
# eval(sys.argv[0])

dimmer(15)