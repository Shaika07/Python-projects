#get phone number information using python

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = phonenumbers.parse("phone number with country code")
print(geocoder.description_for_number(phone_number, 'en'))
print(carrier.name_for_number(phone_number, 'en'))
print(timezone.time_zones_for_number(phone_number))
