ojextends
==============

``ojextends`` allows you to extend the object class and convert ``JSON Documents`` to nested object parsing.

``ojextends`` provides eight key methods to handle transformations.

* `objectToDict` JSON Serialized object `->` dict.
* `objectToStr` JSON Serialized object `->` str.
* `objectsToList` JSON Serialized array of objects `->` list.
* `objectsToStr` JSON Serialized array of objects `->` str.
* `objectFromDict` JSON Serialized object `<-` dict.
* `objectFromStr` JSON Serialized object `<-` str.
* `objectsFromStr` JSON Serialized array of objects `<-` str.
* `objectsFromList` JSON Serialized array of objects `<-` list.



## Getting Started

To install using pip, simply run

```
pip install ojextends
```

Dependencies
------------
``ojextends`` only uses the json library provided by the python system.



Usage
-----
The code below defines some simple models, and its natural mapping to json.

```

  from ojextends import *
  
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
    
```
Example of transformations to parse Area lookup response for item:

```

    import json
    import requests
  from ojextends import *
    
    def get_areas(areaid):
        url = 'https://127.0.0.1/area/lookup?id={}'
        return requests.get(url.format(area_id)).json()

    areajson = get_areas(518000)
    print(areajson)
    
    area = Area.objectToDict(areajson)
    print(area.schools)
    school = area.schools[0] if len(area.schools) else School()
    print(school.name)
```

The code above produces next result:


```

    {
    "name":"shenzhen",
    "student":{
        "name":"Bob",
        "age":20
    },
    "schools":[
        {
            "name":"Shenzhen university",
            "teachers":[
                {
                    "name":"Linda",
                    "students":[
                        {
                            "name":"Bob",
                            "age":20,
                            "books":[
                                "book1",
                                "book2"
                            ]
                        },
                        {
                            "name":"Tom",
                            "age":23
                        }
                    ]
                },
                {
                    "name":"Mike",
                    "students":[
                        {
                            "name":"Lily",
                            "age":18
                        },
                        {
                            "name":"Stone",
                            "age":21
                        }
                    ]
                }
            ]
        },
        {
            "name":"Shenzhen normal university",
            "teachers":[
                {
                    "name":"Linda1",
                    "students":[
                        {
                            "name":"Bob1",
                            "age":20
                        },
                        {
                            "name":"Tom1",
                            "age":23
                        }
                    ]
                },
                {
                    "name":"Mike1",
                    "students":[
                        {
                            "name":"Lily1",
                            "age":18
                        },
                        {
                            "name":"Stone1",
                            "age":21
                        }
                    ]
                }
            ]
        }
    ]
}
```

See tests.py for more examples.


Tests
-----
Getting the tests running looks like:

```

    # Install dependencies
    $ pip install -r requirements.txt
    # Run the test suites
    $ python tests.py
```
License
-------

The MIT License (MIT)

Contributed by `Bob Wu <https://github.com/bob4open/>`