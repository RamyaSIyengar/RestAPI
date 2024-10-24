
import json

courses = '{"name": "Ramya","languages": ["python","selenium","javascript"]}'

# loads method parse json string and return dictionary
dic_courses = json.loads(courses)
print(dic_courses)
print(type(dic_courses))  # <class 'dict'>

print(dic_courses['name'])
print(dic_courses['languages'][2])


