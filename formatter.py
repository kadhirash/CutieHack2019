import string
import re
import os

restaurant = input("Enter a restaurant: ")
if "&" in restaurant:
	restaurant = restaurant.replace("&", "and")
if " " in restaurant:
	restaurant = restaurant.replace(" ", "-")
restaurant = restaurant.translate ({ord(c): "" for c in "!@#$%^*()[]{};:,./<>?\|`~=_+'"})
print(restaurant)

location = input("Enter a city: ")
if "&" in location:
	location = location.replace("&", "and")
if " " in location:
	location = location.replace(" ", "-")
location = location.translate ({ord(c): "" for c in "!@#$%^*()[]{};:,./<>?\|`~=_+'"})
print(location)

graphQL_ID = restaurant + '-' + location
print(graphQL_ID)