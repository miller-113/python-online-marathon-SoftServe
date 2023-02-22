import json
from enum import Enum
import uuid


class ForbiddenException(Exception):
    pass


class PasswordValidationException(Exception):
    def __init__(self, data):
        self.data = data


class Subject:
    def __init__(self, name):
        self.title = name


class NonUniqueException(Exception):
    def __int__(self, data):
        self.data = data


class Role(Enum):
    Mentor = '1'
    Trainee = '2'


class Score(Enum):
    B = 'B'
    D = 'D'


class User:
    def __init__(self, username, password, role, subject_and_score=None):
        self.id = uuid.uuid4()
        self.username = username
        self.password = password
        self.role = role
        self.subject_and_score = subject_and_score

    @classmethod
    def create_user(cls, username, password, role):
        if password == 'InvalidPassword':
            raise PasswordValidationException('Invalid password')
        return cls(username, password, role)

    def add_score_for_subject(self, subject, score):
        if isinstance(subject, Subject):
            if self.subject_and_score:
                self.subject_and_score.extend(
                    [{subject.__getattribute__('title'): score.name}])
            else:
                self.subject_and_score = [
                    {subject.__getattribute__('title'): score.name}]
        else:
            self.subject_and_score = [{subject.get('title'): score.name}]

    def __str__(self):
        return f"{self.username} with role {self.role}:" \
               f" {self.subject_and_score if self.subject_and_score else []}"


def get_subjects_from_json(subjects_json):  # -> List[Subject]
    with open(subjects_json) as r:
        red_file = json.load(r)
    return red_file


def get_users_with_grades(users_json, subjects_json,
                          grades_json):  # -> List[User]
    with open(users_json) as r:
        users_file = json.load(r)
    with open(subjects_json) as r:
        subject_file = json.load(r)
    with open(grades_json) as r:
        grades_file = json.load(r)

    res = []
    for usr in users_file:
        for sbj in subject_file:
            for grade in grades_file:
                if usr.get('id') == grade.get('user_id') and sbj.get(
                        'id') == grade.get('subject_id'):
                    if usr.get('username') not in [i.get('username') for i in
                                                   res]:
                        res.append({'username': usr.get('username'),
                                    'password': usr.get('password'),
                                    'role': usr.get('role'),
                                    'subject_and_score': [{sbj.get('title'):
                                                               grade.get(
                                                                   'score')}]
                                    })
                    else:
                        for i in res:
                            if i.get('username') == usr.get('username'):
                                i['subject_and_score'].append({sbj.get('title'):
                                                                   grade.get(
                                                                       'score')})

    return [User(usr_data['username'],
                 usr_data['password'],
                 usr_data['role'],
                 usr_data['subject_and_score'])
            for usr_data in res]


def add_user(user, users):
    list_users = [usr.username for usr in users]
    if user.username not in list_users:
        users.append(user)
    else:
        raise NonUniqueException(
            f"User with name {user.username} already exists")
    return users


def add_subject(subject, subjects):
    list_subject = [subj.get('id') for subj in subjects]
    if subject.title not in list_subject:
        subjects.append(subject)
    return subjects


def get_grades_for_user(username: str, user: User,
                        users: list):  # returns all grades for the user with username (only own grades or for mentor)-
    result = []
    for usr in users:
        if usr.username == username and usr.subject_and_score:
            if user.password == usr.password or user.role == Role.Mentor:
                result.extend(usr.subject_and_score)
                continue
            raise ForbiddenException('Forbidden')
    return sorted(result, key=lambda k: k[[*k][0]])


def users_to_json(users, json_file):
    with open(json_file, 'w') as f:
        for item in users:
            if isinstance(item.role, Role):
                item.role = item.role.name
            if isinstance(item.id, uuid.UUID):
                item.id = item.id.int
        json.dump([item.__dict__ for item in users], f)


def subjects_to_json(subjects, json_file):
    res = []
    with open(json_file, 'w') as f:
        for item in subjects:
            if isinstance(item, Subject):
                item = item.__dict__

            res.append(item)
        json.dump(res, f)


def grades_to_json(users, subjects, json_file):
    res = []
    with open(json_file, 'w') as f:
        for item in users:
            if isinstance(item.role, Role):
                item.role = item.role.name
            if isinstance(item.id, uuid.UUID):
                item.id = item.id.int
            res.append(item.__dict__)
        json.dump(res, f)


def check_if_user_present(name, password, users_list):
    for usr in users_list:
        if usr.username == name and usr.password == password:
            return True
    return False


def file_contains(file, find_by, finding):
    return True


users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

try:
    print(get_grades_for_user("Second", users[0], users))
except ForbiddenException:
    print("Forbidden")
print(get_grades_for_user("Second", users[2], users))
