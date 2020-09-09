#Get Colorado Covid Data from the State of Colorado
import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)

url = "http://data.sfgov.org/resource/rqzj-sfat.json"
r = requests.get(url)
print(type(r))
data = r.json()
pp.pprint(data)

