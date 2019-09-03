#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import copy
import decimal
import datetime
import unittest
from mock import MagicMock

import ojextends as JsonSerializable


TEST_INPUT = {
    'name': 'shenzhen',
    'schools': [
        {
            'name': 'shenzhen universty', 
            'teachers': [
                {
                    'name': 'Linda', 
                    'students': [
                        {
                            'name':'Bob', 
                            'age': 20
                        },
                        {
                            'name':'Tom', 
                            'age': 23
                        }
                    ]
                },
                {
                    'name': 'Mike', 
                    'students': [
                        {
                            'name':'Lily', 
                            'age': 18
                        },
                        {
                            'name':'Stone', 
                            'age': 21
                        }
                    ]
                }
            ]
        }
    ]
}



@JsonSerializable
class Student(object):
  name  = str
  age   = int
  books = list

@JsonSerializable
class Teacher(object):
  name      = str
  students  = list([Student])

@JsonSerializable
class School(object):
  name      = str
  teachers  = list([Teacher])

@JsonSerializable
class Area(object):
  name    = str
  schools = list([School])
  school  = School
  student = Student


class ObjectJsonExtendsTestCase(unittest.TestCase):

    def test_default_value(self):
        data = {'x': {'y': [1, 2], '1': [3, 4], '?': 'any'}}
        # self.assertEqual(Path('x', allow_null=True).find({'x': None}), None)

    def test_objects(self):
        data = {'x': {'y': 1, 'z': [3, 4]}}
        # self.assertEqual(find('x.y', data, 'jmespath'), 1)
        # self.assertRaises(GenericError, find, 'x.y', data, 'dummy')


if __name__ == '__main__':
    unittest.main()
