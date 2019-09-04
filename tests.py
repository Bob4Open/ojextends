from ojextends import JsonSerializable
import json

@JsonSerializable
class Student(object):
	name = str
	age = int
	books = list

@JsonSerializable
class Teacher(object):
	name = str
	students = list([Student])

@JsonSerializable
class School(object):
	name = str
	teachers = list([Teacher])

@JsonSerializable
class Area(object):
	name = str
	schools = list([School])
	school = School
	student = Student

def printJson(data):
	print(json.dumps(data, indent=4, sort_keys=True))	

if __name__ == '__main__':
	jsonstr = '{"name": "shenzhen","student": {"name":"Bob", "age": 20}, "schools": [{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20, "books": ["book1", "book2"]},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]},{"name": "shenzhen other universty", "teachers": [{"name": "Linda1", "students": [{"name":"Bob1", "age": 20},{"name":"Tom1", "age": 23}]},{"name": "Mike1", "students": [{"name":"Lily1", "age": 18},{"name":"Stone1", "age": 21}]}]}]}'
	# jsonstr = '[{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]}]'
	jsondict = dict({'name': 'shenzhen','student': {'name':'Bob', 'age': 20}, 'schools': [{'name': 'shenzhen universty', 'teachers': [{'name': 'Linda', 'students': [{'name':'Bob', 'age': 20},{'name':'Tom', 'age': 23}]},{'name': 'Mike', 'students': [{'name':'Lily', 'age': 18},{'name':'Stone', 'age': 21}]}]},{'name': 'shenzhen other universty', 'teachers': [{'name': 'Linda1', 'students': [{'name':'Bob1', 'age': 20},{'name':'Tom1', 'age': 23}]},{'name': 'Mike1', 'students': [{'name':'Lily1', 'age': 18},{'name':'Stone1', 'age': 21}]}]}]})
	jsonlist = list([{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]}])

	area = Area.objectFromDict(jsondict)
	printJson(area.objectToStr())

