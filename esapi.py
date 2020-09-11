import requests
import simplejson as json
import pprint


uri = "http://ec2-54-214-200-23.us-west-2.compute.amazonaws.com:9200/codata/_search"
pp = pprint.PrettyPrinter(indent=2)
def testsearch(uri):
  """Simple Elasticsearch Query"""
  query = json.dumps({

    "query" : {"multi_match" : {
      "query" : "CO",
      "fields" : ["STATE", "CITY", "ADDRESS", "ZIP", "SITE", "COUNTY"],
      "type":     "most_fields"
    }}
  })

  response = requests.get(uri,   headers={"Content-type":"application/json"}, data=query)
  print(response.json())
  results = json.loads(response.text)
  pp.pprint(results)
  return results

  #pp.pprint(results)


res = testsearch(uri)




