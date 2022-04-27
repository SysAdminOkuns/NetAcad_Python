one_gallon_to_liters = 3.785411784
one_mile_to_meters = 1609.344
one_km_to_meters = 1000    
def liters_100km_to_miles_gallon(liters):
    x_gallons = liters / one_gallon_to_liters
    return ((one_km_to_meters * 100) / one_mile_to_meters) / x_gallons

def miles_gallon_to_liters_100km(miles):
    x_kilometers = miles * one_mile_to_meters / 100 / 1000 
    return one_gallon_to_liters / x_kilometers
#
# Write your code here
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
