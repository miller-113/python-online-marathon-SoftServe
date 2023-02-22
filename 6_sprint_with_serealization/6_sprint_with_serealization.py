"""
Create function find(file, key)
This function parses json-file and returns all unique values of the key.

1.json:
[{"name": "user_1", "password": "pass_1"},
{"name": "user_2", "password": ["pass_1", "qwerty“]} ]
find("1.json", "password") returns ["pass_1", "qwerty"]

2.json: [{"name": "user_1", "credentials": {"username": "user_user",
"password": "1234qweQWE"}}, {"name": "user_2", "password": ["pass_1 ",
"qwerty "]}] find("2.json", "password") returns ["1234qweQWE", "pass_1",
"qwerty"]

3.json: {"name": "user_1","credentials": {"username": "user_user","password":
"1234qweQWE"}} find("3.json", "password") returns ["1234qweQWE"]
"""

# Task1
# import json
# import ast
# import re


# def find(file, key):
#     with open(file, 'r', encoding='utf-8') as file:
#         data = file.read()
#         temp = re.findall(rf'(?<={key}\":.)\[?\'?\"?([\w\s\'",]*)\]?', data)
#         return list(set(
#             re.findall(r'\w+\s?', ' '.join([key for str_ in temp
#                                             for key in str_.split(',')]))))
#
#
# print(find("1.json", "password"))

# EndTask


"""Implement function parse_user(output_file, *input_files) for creating file 
that will contain only unique records (unique by key "name") by merging 
information from all input_files argument (if we find user with already 
existing name from previous file we should ignore it). Use pretty printing 
for writing users to json-file. 


If the function cannot find input files we need to log information with error 
level 

root - ERROR - File <file name> doesn't exist

For example:
user1.json : 
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
]

user2.json : 
[{"name": "Bob1", "rate": 25, “languages": ["French"]},
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

If we execute parse_user(user3.json, user1.json, user2.json)
then file user3.json should contain information:
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]
"""

# Task2 !!!

# import logging
#
#
# def parse_user(output_file, *input_files):
#
#     check = []
#     result = []
#     input_files_uniq = []
#     try:
#         if not input_files:
#             raise FileNotFoundError
#         for i in input_files:
#             with open(i, 'r') as file:
#                 file.w
#                 json_file = json.load(file)
#                 for inner_dict in json_file:
#                     if inner_dict.get('name') not in check and \
#                             inner_dict.get('name'):
#                         check.append(inner_dict.get('name'))
#                         result.append(inner_dict)
#                         input_files_uniq.append(i)
#
#         with open(output_file, 'w') as write_file:
#             json.dump(result, write_file, indent=4)
#     except FileNotFoundError as e:
#         logging.basicConfig(filename='app.log', filemode='w',
#                             format='%(name)s - %(levelname)s - %(message)s')
#         logger = logging.getLogger('root')
#
#         [logger.error(f'File {text_err} doesn\'t exist')
#          for text_err in input_files if text_err not in input_files_uniq]
#     return result
#
#
# print(parse_user('test.json', './jsons_to_6sprint/user1.json',
#                  './jsons_to_6sprint/user2.json'))

# EndTask


# TASK4
# import json
# from json import JSONEncoder
#
# class Student:
#     def __init__(self, full_name, avg_rank, courses):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses
#
#     @classmethod
#     def from_json(cls, data):
#         with open(data, 'r') as file:
#             d = json.load(file)
#         return Student(**d)
#
#
#     # @classmethod
#     def serialize_to_json(self, file):
#         with open(file, 'w') as f:
#             return json.dump({"full_name": self.full_name,
#                               "avg_rank": self.avg_rank,
#                               "courses": self.courses}, f)
#
#     def __str__(self):
#         return f'{self.full_name} ({self.avg_rank}): {self.courses}'
#
# class Group:
#     def __init__(self, title, students):
#         self.title = title
#         self.students = students
#
#     @staticmethod
#     def serialize_to_json(list_of_groups, filename):
#         d_to_save = []
#         with open(filename, 'w') as w_file:
#             # for data in list_of_groups:
#
#             return json.dump([{'title': i.title.split('.')[0],
#                               'students': i.students
#                               if i.title != '2020-01.json'
#                               else [i.students]}
#                               for i in list_of_groups], w_file)
#
#     @classmethod
#     def create_group_from_file(cls, students_file):
#         with open(students_file, 'r') as file:
#             data = json.load(file)
#         return Group(**{'title': students_file, 'students': data})
#
#     def __str__(self):
#         title = str(self.title).split('.')[0]
#         student_inf = self.students
#         if isinstance(student_inf,list):
#             return f'{title}: [' + f', '\
#                 .join([f"\"{i.get('full_name')} ({i.get('avg_rank')}):"
#                        f" {[z for z in i.get('courses')]}\""
#                        for i in student_inf]) + ']'
#         return f"{title}: [\"{student_inf.get('full_name')}" \
#                f" ({student_inf.get('avg_rank')}):" \
#                f" {student_inf.get('courses')}\"]"
# g1 = Group.create_group_from_file("./2020-2.json")
# g2 = Group.create_group_from_file("./2020-01.json")
# Group.serialize_to_json([g1, g2], "g1.json")
# # print_file("g1")
# # g1 = Group.create_group_from_file("2020_2.json")
# print(g1)
# print(g2)
# ENDTASK


"""In user.json file we have information about users in format [{“id”: 1, 
“name”: “userName”, “department_id”: 1}, ...], 

in file department.json are information about departments in format: [{“id”: 
1, “name”: “departmentName”}, ...]. 

Function user_with_department(csv_file, user_json, department_json) should 
read from json files information and create csv file in format: 

header line - name, department

next lines :  <userName>, <departmentName>

If file department.json doesn't contain department with department_id from 
user.json we generate DepartmentName exception. 

Create appropriate json-schemas for user and department.

If schema for user or department doesn't satisfy formats described above we 
should generate InvalidInstanceError exception 

To validate instances create function validate_json(data, schema)
"""

# TASK3

# import json
# import jsonschema
# from jsonschema import validate
# import csv
#
#
# class DepartmentName(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return self.data
#
#
# class InvalidInstanceError(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return self.data
#
#
# schema_DepartmentName = {
#     'type': 'object',
#     'required': ['id']
# }
#
# schema_InvalidInstanceError = {'properties': {'id': {'type': 'number'},
#                                               'name': {'type': 'string'}},
#      'required': ['id', 'name'],
#      'type': 'object'}
#
#
# def validate_json(data, schema):
#     try:
#         for d in data:
#             validate(d, schema)
#     except Exception as e:
#         if "None is not of type 'number'" in e.message:
#             print('12342')
#             raise InvalidInstanceError('Error in user schema')
#             exit(0)
#         else:
#             # raise DepartmentName('Error in department schema')
#             print('Error in department schema')
#             exit(0)
#             # raise InvalidInstanceError('Error in user schema')
#
#
# def read_json(json_file):
#     with open('./'+json_file, 'r') as file:
#         json_file_ = json.load(file)
#     return json_file_
#
#
# def user_with_department(csv_file, user_json, department_json):
#     user_json_red = read_json(user_json)
#     department_json_red = read_json(department_json)
#     departament_ids_users = [id_.get('department_id')
#                              for id_ in user_json_red]
#     departament_ids = [id_.get('id') for id_ in department_json_red]
#
#
#     validate_json(user_json_red, schema_InvalidInstanceError)
#     validate_json(department_json_red, schema_DepartmentName)
#
#
#     try:
#         for dep_id in departament_ids_users:
#             if dep_id == None:
#                 raise InvalidInstanceError('Error in user schema')
#             if dep_id not in departament_ids:
#                 raise DepartmentName(f'Department with id {dep_id}'\
#                                      f'doesn\'t exists')
#     except DepartmentName as e:
#         print(e)
#
#     with open(csv_file, 'w', encoding='utf8', newline='') as file:
#         header = ['name', 'department']
#         writer = csv.writer(file)
#         writer.writerow(header)
#         for user in user_json_red:
#             writer.writerow([user.get('name'),
#                              'Dep ' + str(user.get('department_id'))])
#
#
# user_with_department("user_department.csv", "user.json", "department.json")

# END TASK
"""Create context manager class SerializeManager with attributes filename and 
type for serializing python object to different formats. This class should 
contain method serialize for serialize object to filename according to  type. 
For defining format create enum FileType with values JSON, BYTE. Create 
function serialize(object, filename, filetype). This function use 
SerializeManager and should serialize object to filename according to type. 
For example: if user_dict = { 'name': 'Roman', 'id': 8} then serialize(
user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file 
will contain user_dict as byte array serialize("String", "string.json", 
FileType.JSON) -> creates file with name "string.json" and text "String" """
# TASK 5

# import json
# import pickle
# from enum import Enum
#
#
# class FileType(Enum):
#     JSON = 'JSON'
#     BYTE = 'BYTE'
#
#
# class SerializeManager:
#     def __init__(self, filename, filetype):
#         self.filename = filename
#         self.filetype = filetype
#
#     def __enter__(self):
#         return self
#
#     def serialize(self, data):
#         if self.filetype.name == 'BYTE':
#             file = open(self.filename, 'wb')
#             pickle.dump(str(data), file)
#             return file.close()
#         file = open(self.filename, 'w')
#         json.dump(data, file)
#         return file.close()
#
#     def __exit__(self, *args):
#         if args[0]:
#             print(f'Erros with {args[0].__name__} with name {args[1]}')
#
#
# def serialize(object, filename, fileType):
#     with SerializeManager(filename, fileType) as manager:
#         manager.serialize(object)
#
#
# # serialize(user_dict, 'filename.json', FileType.JSON)
# user_dict = {"name": "Hallo", "id": 2}
# serialize(user_dict, "2.json", FileType.JSON)
# with open("2.json", "r") as file:
#     print(json.load(file))


# TASK 1_2 not mine, via recursion
# import json
#
#
# def find_all(data, key):
#     result = []
#
#     def find_in_dict(data, key):
#         for k, v in data.items():
#             if k == key:
#                 result.extend(v) if isinstance(v, list) else result.append(v)
#             else:
#                 find_in_list(data, key)
#
#     def find_in_list(data, key):
#         if isinstance(data, list):
#             for list_elem in data:
#                 find_in_list(list_elem, key)
#         if isinstance(data, dict):
#             find_in_dict(data, key)
#
#     find_in_list(data, key)
#     return set(result)
#
#
# def find(file, key):
#     with open(file) as json_file:
#         data = json.load(json_file)
#     return list(find(data, key))

# END TASK

# TASK 2 not mine
# import json
# import logging
#
#
# def parse_user(output_file, *input_files):
#     key_for_parse = 'name'
#     data_from_json = []
#     set_of_unique_names = []
#     users = []
#     for user in input_files:
#         try:
#             with open(user) as json_file:
#                 data_from_json.extend(json.load(json_file))
#         except:
#             logging.error(f"File {user} doesn't exist")
#     for dict1 in data_from_json:
#         for k, v in dict1.items():
#             if (k == key_for_parse and v not in set_of_unique_names):
#                 set_of_unique_names.append(v)
#                 users.append(dict1)
#
#     with open(output_file, 'w') as file:
#         json.dump(users, file, indent=4)

# END TASK



# EXAMPLES WORKS DIFFERENT LOAD AND LOADS

# from io import StringIO
# import json
#
# fileObj = StringIO('{"Geeks": "for Geeks"}')
# print("Using json.load(): "+str(json.load(fileObj)))
# print("Using json.loads(): "+str(json.loads('{"Geeks": "for Geeks"}')))
# print("Using json.JSONDecoder().decode(): " +
#     str(json.JSONDecoder().decode('{"Geeks": 1, "for": 2, "Geeks": 3}')))
# print("Using json.JSONDecoder().raw_decode(): " +
#     str(json.JSONDecoder().raw_decode('{"Geeks": 1,
#                                         "for": 2, "Geeks": 322}')))
# iter()
