import datetime
import re

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.utils import DataError, IntegrityError
from django.utils import timezone

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)


class CustomUser(AbstractBaseUser):
    """
        This class represents a basic user. \n
        Attributes:
        -----------
        param first_name: Describes first name of the user
        type first_name: str max length=20
        param last_name: Describes last name of the user
        type last_name: str max length=20
        param middle_name: Describes middle name of the user
        type middle_name: str max length=20
        param email: Describes the email of the user
        type email: str, unique, max length=100
        param password: Describes the password of the user
        type password: str
        param created_at: Describes the date when the user was created. Can't be changed.
        type created_at: int (timestamp)
        param updated_at: Describes the date when the user was modified
        type updated_at: int (timestamp)
        
        param role: user role, default role (0, 'visitor')
        type updated_at: int (choices)
        param is_active: user role, default value False
        type updated_at: bool

    """
    # id = models.IntegerField(primary_key=True, null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.IntegerField(choices=ROLE_CHOICES,
                               default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at,
                 user role, user is_active
        """
        return f"'id': {self.id}, " \
               f"'first_name': '{self.first_name}', " \
               f"'middle_name': '{self.middle_name}', " \
               f"'last_name': '{self.last_name}', " \
               f"'email': '{self.email}', " \
               f"'created_at': {self.created_at.timestamp():.0f}, " \
               f"'updated_at': {self.updated_at.timestamp():.0f}, " \
               f"'role': {self.role}, " \
               f"'is_active': {self.is_active}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of CustomUser object.
        :return: class, id
        """
        return f"CustomUser(id={self.id})"

    @staticmethod
    def get_by_id(user_id):
        """
        :param user_id: SERIAL: the id of a user to be found in the DB
        :return: user object or None if a user with such ID does not exist
        """
        try:
            specific_user = CustomUser.objects.get(id=user_id)
        except ObjectDoesNotExist:
            specific_user = None
        return specific_user

    @staticmethod
    def get_by_email(email):
        """
        Returns user by email
        :param email: email by which we need to find the user
        :type email: str
        :return: user object or None if a user with such ID does not exist
        """
        try:
            specific_user = CustomUser.objects.get(email=email)
        except ObjectDoesNotExist:
            specific_user = None
        return specific_user

    @staticmethod
    def delete_by_id(user_id):
        """
        :param user_id: an id of a user to be deleted
        :type user_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            specific_user = CustomUser.objects.get(id=user_id)
            specific_user.delete()
        except ObjectDoesNotExist:
            specific_user = None
        return specific_user

    @staticmethod
    def create(email, password, first_name=None, middle_name=None,
               last_name=None):
        """
        :param first_name: first name of a user
        :type first_name: str
        :param middle_name: middle name of a user
        :type middle_name: str
        :param last_name: last name of a user
        :type last_name: str
        :param email: email of a user
        :type email: str
        :param password: password of a user
        :type password: str
        :return: a new user object which is also written into the DB
        """

        regex_for_mail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        try:
            if re.fullmatch(regex_for_mail, email):
                new_user = CustomUser(email=email,
                                      password=password,
                                      first_name=first_name,
                                      middle_name=middle_name,
                                      last_name=last_name)
                new_user.save()
            else:

                raise DataError
        except (DataError, IntegrityError):
            new_user = None
        return new_user

    def to_dict(self):
        """
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at, user is_active
        :Example:
        | {
        |   'id': 8,
        |   'first_name': 'fn',
        |   'middle_name': 'mn',
        |   'last_name': 'ln',
        |   'email': 'ln@mail.com',
        |   'created_at': 1509393504,
        |   'updated_at': 1509402866,
        |   'role': 0
        |   'is_active:' True
        | }
        """
        return_value = {
           'id': self.id,
           'first_name': self.first_name,
           'middle_name': self.middle_name,
           'last_name': self.last_name,
           'email': self.email,
           'created_at': int(f'{self.created_at.timestamp():.0f}'),
           'updated_at': int(f'{self.updated_at.timestamp():.0f}'),
           'role': self.role,
           'is_active': self.is_active,
        }
        return return_value

    def update(self,
               first_name=None,
               last_name=None,
               middle_name=None,
               password=None,
               role=None,
               is_active=None):
        """
        Updates user profile in the database with the specified parameters.\n
        :param first_name: first name of a user
        :type first_name: str
        :param middle_name: middle name of a user
        :type middle_name: str
        :param last_name: last name of a user
        :type last_name: str
        :param password: password of a user
        :type password: str
        :param role: role id
        :type role: int
        :param is_active: activation state
        :type is_active: bool
        :return: None
        """
        # obj_to_update = {
        self.first_name = first_name if first_name else self.first_name
        self.last_name = last_name if last_name else self.last_name
        self.middle_name = middle_name if middle_name else self.middle_name
        self.password = password if password else self.password
        self.role = role if role else self.role
        self.is_active = is_active if is_active else self.is_active
        self.save()
        return self

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all users
        """
        return CustomUser.objects.all()

    def get_role_name(self):
        """
        returns str role name
        """
        for i in ROLE_CHOICES:
            if i[0] == self.role:
                return i[1]
        return None


