
import wrapt
import types
import sys
import json

customType = list()
originType = [str,int,list,dict,tuple,float,long,bool,unicode]

def objectToDict(self):
	result = dict()
	for key, value in self.__dict__.iteritems():
		if type(value).__name__ == 'list':
			result[key] = map(lambda item: item.objectToDict(),value)
		elif type(value).__name__ in customType :
			result[key] = value.objectToDict()
		else:
			result[key] = self.__dict__[key]
	return result

def objectToStr(self):
	pass

def objectsToList(self):
		pass

def objectsToStr(self):
	pass

@classmethod
def objectFromDict(cls, pDict):
	# print('{} 111'.format(cls))
	instance = cls()
	# print('{} 222'.format(instance))
	for key, value in pDict.iteritems():
		# print(type(value))
		if type(value).__name__ == 'dict' :
			setattr(instance, key, getattr(instance,key).objectFromDict(value))
		elif type(value).__name__ == 'list' :
			# setattr(cls, key, )
			# print(value[0])
			# print('key: {}, value: {}'.format(key,value))
			# print('clz1 {} {}'.format(instance,key))
			clz = list(getattr(instance, key))[0]
			# print('clz {}'.format(getattr(instance, key)))
			setattr(instance, key, clz.objectsFromList(value))
			pass
		else:
			setattr(instance, key, value)
	# print('{} key: objectFromDict'.format(cls.__name__))
	return instance

@classmethod
def objectsFromList(cls, pList):
	# print(cls)
	lists = list()
	# print(len(pList))
	for item in pList:
		instance = cls()
		# print(type(item))
		if type(item).__name__ == 'dict' :
			# print('3333 {} {}'.format(cls, item))
			instance = cls.objectFromDict(item)
		elif type(item).__name__ == 'list' :
			# setattr(cls, key, )
			# print(value[0])
			# print('key: {}, value: {}'.format(key,value))
			pass
		else:
			pass
		lists.append(instance)
		# 	setattr(instance, key, value)
	# print('{} key: objectFromDict'.format(cls.__name__))
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

# @wrapt.decorator
# def JsonSerializable(wrapped, instance, args, kwargs):
# 	print("[DEBUG]: enter {}()".format( wrapped.__name__))
# 	# clazz = globals()['Area']
# 	# instance = clazz()
# 	instance.objectToDict = objectToDict
# 	instance.objectToStr = objectToStr
# 	instance.objectFromDict = objectFromDict
# 	instance.objectsFromList = objectsFromList
# 	instance.objectFromStr = objectFromStr
# 	instance.objectsFromStr = objectsFromStr
# 	print(type(wrapped))
# 	return wrapped(*args, **kwargs)

def JsonSerializable(cls):
	cls.objectToDict = objectToDict
	cls.objectToStr = objectToStr
	cls.objectFromDict = objectFromDict
	cls.objectsFromList = objectsFromList
	cls.objectFromStr = objectFromStr
	cls.objectsFromStr = objectsFromStr
	if not cls.__name__ in customType:
		customType.append(cls.__name__)
# 	# Area.objectFromDict = types.MethodType(objectFromDict,Area)
	return cls
	
# from array import array

@JsonSerializable
class Student(object):
	name = str
	age = int

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
	# def __init__(self):
	# 	pass
		
	# def objectToDict():
	# 	pass

	# @property
	# def objectToStr():
	# 	pass
	
	# @classmethod
	# def objectFromDict(cls, dict):
	# 	clazz = globals()['Area']
	# 	instance = clazz()
	# 	# instance = Area()
	# 	instance.dict = dict
	# 	return instance

	# @classmethod
	# def objectsFromDict(cls, dict):
	# 	pass

	# @classmethod
	# def objectFromStr(cls, str):
	# 	pass

	# @classmethod
	# def objectsFromStr(cls, str):
	# 	pass


		
if __name__ == '__main__':
	jsonstr = '{"name": "shenzhen","student": {"name":"Bob", "age": 20}, "schools": [{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]},{"name": "shenzhen other universty", "teachers": [{"name": "Linda1", "students": [{"name":"Bob1", "age": 20},{"name":"Tom1", "age": 23}]},{"name": "Mike1", "students": [{"name":"Lily1", "age": 18},{"name":"Stone1", "age": 21}]}]}]}'
	# jsonstr = '[{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]}]'
	jsondict = dict({'name': 'shenzhen','student': {'name':'Bob', 'age': 20}, 'schools': [{'name': 'shenzhen universty', 'teachers': [{'name': 'Linda', 'students': [{'name':'Bob', 'age': 20},{'name':'Tom', 'age': 23}]},{'name': 'Mike', 'students': [{'name':'Lily', 'age': 18},{'name':'Stone', 'age': 21}]}]},{'name': 'shenzhen other universty', 'teachers': [{'name': 'Linda1', 'students': [{'name':'Bob1', 'age': 20},{'name':'Tom1', 'age': 23}]},{'name': 'Mike1', 'students': [{'name':'Lily1', 'age': 18},{'name':'Stone1', 'age': 21}]}]}]})
	jsonlist = list([{"name": "shenzhen universty", "teachers": [{"name": "Linda", "students": [{"name":"Bob", "age": 20},{"name":"Tom", "age": 23}]},{"name": "Mike", "students": [{"name":"Lily", "age": 18},{"name":"Stone", "age": 21}]}]}])

	# area = Area.objectFromDict(jsondict)
	# area = Area.objectFromDict(jsondict)				
	# print(area)
	# print(dir(area))
	# print(hasattr(area, 'objectFromDict'))
	# print(area.name)
	# print(Area.name)
	# print(area.schools)
	# print(area.school.__name__)
	# s = Area()
	# print(s.name)
	# print(student.age)
	# print(area.schools[1].name)


	# areas = Area.objectsFromList(jsonlist)
	# print(areas[0].name)

	area = Area.objectFromStr(jsonstr)
	# print(area.schools[0].name)

	# schools = School.objectsFromStr(jsonstr)
	# print(schools[0].teachers[0].name)
	print(area.objectToDict())

	# print(json.loads(jsonstr))

