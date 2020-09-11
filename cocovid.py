#Get Colorado Covid Data from the State of Colorado
import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)
#url = "http://data.sfgov.org/resource/rqzj-sfat.json"
url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/Community_Testing_Sites/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"

r = requests.get(url)
print(type(r))
#print(r)
data = r.json()
attributes = data['features']
pp.pprint(attributes)

#pp.pprint(data)

