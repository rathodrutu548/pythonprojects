import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

a=input("Enter your phone number: ")
# to read the number
phone_number=phonenumbers.parse(a)
# to print the country name
print(geocoder.description_for_number(phone_number,"en"))
# to print the carriername
print(carrier.name_for_number(phone_number,"en"))
