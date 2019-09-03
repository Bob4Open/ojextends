
__all__ = ['List', 'JsonSerializable', 'objectToDict','objectToStr',
		'objectFromDict','objectFromStr','objectsFromStr',
		'objectsFromList','objectsToList','objectsToStr']

import json

originType = (str,int,float,long,bool,list,dict,tuple,unicode,set)

def objectToDict(self):
	result = dict()
	for key, value in self.__dict__.iteritems():
		if isinstance(value, originType) :
			if isinstance(value, list) :
				result[key] = map(lambda item: (item if isinstance(item, originType) else item.objectToDict()), value)
			else:
				result[key] = self.__dict__[key]
		else :
			result[key] = value.objectToDict()
	return result

def objectToStr(self):
	return str(self.objectToDict())

def objectsToList(self):
	return map(lambda item: item.objectToDict(), self)

def objectsToStr(self):
	return str(objectsToList(self))

@classmethod
def objectFromDict(cls, pDict):
	instance = cls()
	for key, value in pDict.iteritems():
		if type(value).__name__ == 'dict' :
			setattr(instance, key, getattr(instance,key).objectFromDict(value))
		elif type(value).__name__ == 'list' :
			if not isinstance(getattr(instance, key), list):
				clz = list(getattr(instance, key))[0]
				setattr(instance, key, clz.objectsFromList(value))
			else:
				setattr(instance, key, value)
		else:
			setattr(instance, key, value)
	return instance

@classmethod
def objectsFromList(cls, pList):
	lists = List()
	for item in pList:
		instance = cls()
		if type(item).__name__ == 'dict' :
			instance = cls.objectFromDict(item)
		elif type(item).__name__ == 'list' :
			pass
		else:
			pass
		lists.append(instance)
	return lists

@classmethod
def objectFromStr(cls, str):
	result = json.loads(str)
	if type(result).__name__ == 'dict':
		return cls.objectFromDict(result)
	elif type(result).__name__ == 'list':
		return cls.objectsFromList(result)
	return None

@classmethod
def objectsFromStr(cls, str):
	result = json.loads(str)
	if type(result).__name__ == 'list':
		return cls.objectsFromList(result)	
	return None

def JsonSerializable(cls):
	cls.objectToDict 	= objectToDict
	cls.objectToStr 	= objectToStr
	cls.objectFromDict 	= objectFromDict
	cls.objectFromStr 	= objectFromStr
	cls.objectsFromStr 	= objectsFromStr
	cls.objectsFromList = objectsFromList
	cls.objectsToList 	= objectsToList
	cls.objectsToStr 	= objectsToStr
	return cls

@JsonSerializable
class List(list):
	pass
		
# @JsonSerializable
# class Student(object):
# 	name = str
# 	age = int
# 	books = list

# @JsonSerializable
# class Teacher(object):
# 	name = str
# 	students = list([Student])

# @JsonSerializable
# class School(object):
# 	name = str
# 	teachers = list([Teacher])

# @JsonSerializable
# class Area(object):
# 	name = str
# 	schools = list([School])
# 	school = School
# 	student = Student

def printJson(data):
	print json.dumps(data, indent=4, sort_keys=True)		

# if __name__ == '__main__':
# 	jsonstr = '{"name": "shenzhen","student": {"name":"Bob", "age": 20}, "schools": [{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20, "books": ["book1", "book2"]},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]},{"name": "shenzhen other universty", "teachers": [{"name": "Linda1", "students": [{"name":"Bob1", "age": 20},{"name":"Tom1", "age": 23}]},{"name": "Mike1", "students": [{"name":"Lily1", "age": 18},{"name":"Stone1", "age": 21}]}]}]}'
# 	# jsonstr = '[{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]}]'
# 	jsondict = dict({'name': 'shenzhen','student': {'name':'Bob', 'age': 20}, 'schools': [{'name': 'shenzhen universty', 'teachers': [{'name': 'Linda', 'students': [{'name':'Bob', 'age': 20},{'name':'Tom', 'age': 23}]},{'name': 'Mike', 'students': [{'name':'Lily', 'age': 18},{'name':'Stone', 'age': 21}]}]},{'name': 'shenzhen other universty', 'teachers': [{'name': 'Linda1', 'students': [{'name':'Bob1', 'age': 20},{'name':'Tom1', 'age': 23}]},{'name': 'Mike1', 'students': [{'name':'Lily1', 'age': 18},{'name':'Stone1', 'age': 21}]}]}]})
# 	jsonlist = list([{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]}])

# 	# area = Area.objectFromDict(jsondict)
# 	# area = Area.objectFromDict(jsondict)				
# 	# print(area)
# 	# print(dir(area))
# 	# print(hasattr(area, 'objectFromDict'))
# 	# print(area.name)
# 	# print(Area.name)
# 	# print(area.schools)
# 	# print(area.school.__name__)
# 	# s = Area()
# 	# print(s.name)
# 	# print(student.age)
# 	# print(area.schools[1].name)


# 	# areas = Area.objectsFromList(jsonlist)
# 	# print(areas[0].name)

# 	area = Area.objectFromStr(jsonstr)
# 	# print(area.schools[0].name)
# 	printJson(area.objectToDict()) 
# 	# print(area.objectToDict(), intent = 2)

# 	# schools = School.objectsFromList(jsonlist)
# 	# print(schools[0].teachers[0].name)
# 	# print(type(schools).__name__)
# 	# print(objectsToStr(schools))
# 	# print(schools.objectsToStr())
# 	# ls = List()
# 	# print(isinstance(ls, originType))
# 	# print(isinstance(area, object))
# 	# print(originType)
# 	# lt = list()
# 	# lt = lt + schools
# 	# print(lt)

# 	# print inspect.getargspec(area.objectsToStr)  # failed
# 	# print inspect.getsource(area.objectsToStr)  # failed
# 	# print(json.loads(jsonstr))

