import json

text = '''{
  "data" : [
  {
    "location": "New York, USA",
    "summary": "A vibrant city"
  },
  {
    "location": "Los Angeles, USA",
    "summary": "City of Angels"
  },
  {
    "location": "San Francisco, USA",
    "summary": "Tech hub by the bay"
  }
]
}
'''
data = json.loads(text)
data["usage"] = "usage"
print(data["usage"])