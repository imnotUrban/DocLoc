import json

text = '''[
  {
    "location": "New York",
    "summary": "A vibrant city"
  },
  {
    "location": "Los Angeles",
    "summary": "City of Angels"
  },
  {
    "location": "San Francisco",
    "summary": "Tech hub by the bay"
  }
]
'''
data = json.loads(text)
print(data)