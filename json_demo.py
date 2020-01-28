import json

insertIntoJobsList = '''
{
    "people": [
    {
        "name": "John Smith",
        "phone": "615-555-7164",
        "email": ["john.smith@notreal.com", "johnsmith@fakeemail.com"],
        "has_license": false
        },
        {
        "name": "Jane Doe",
        "phone": "560-555-5153",
        "email": null,
        "has_license": true
        }
        ]
        }
'''

data = json.loads(insertIntoJobsList)
# print(type(data))
# print(data)

for person in data['people']:
#     print(person)
#     print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2)

print(new_string)
