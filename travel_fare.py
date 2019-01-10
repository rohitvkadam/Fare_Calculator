import json
import requests

key_gooogl = "AIzaSyD47lFWmSVHBvtZzqneAOWko6ZgOMLKOgo"
type_commute = input("Please select your commute for ride:")
source = input("Select your source :")
destination = input("Select your destination :")

url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+source+"&destinations="+destination+"&mode=driving&units=metric&key="+key_gooogl

ans = requests.get(url)
result = json.loads(ans.text)
distance_value = result['rows'][0]['elements'][0]['distance']['value']
km = distance_value/1000

if type_commute == "bus":
    fare_calc_bus = km*10
    print('From {} to {} is {} km \nTotal fair is {} Rs.'.format(source,destination,km,fare_calc_bus))
elif type_commute == "rikshaw":
    fare_calc_rik = km*18
    print('From {} to {} is {} km \n Total fair is {} Rs.'.format(source,destination,km,fare_calc_rik))
elif type_commute == "cab":
    fare_calc_cab = km*30
    print('From {} to {} is {} km \n Total fair is {} Rs.'.format(source,destination,km,fare_calc_cab))
else:
    print('invalid selection.')








