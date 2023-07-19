import phonenumbers
from phonenumbers import timezone
import time 

while True:
	
	o =input('>>>')

	x = phonenumbers.parse(o)

	timeZone = timezone.time_zones_for_number(x)
	print(''.join(timeZone))