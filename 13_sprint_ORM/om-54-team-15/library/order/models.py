from django.db import models
from django.utils import timezone

from book import models as b_model
from authentication import models as a_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import DataError, IntegrityError


class Order(models.Model):

    book = models.ForeignKey(b_model.Book, on_delete=models.CASCADE)
    user = models.ForeignKey(a_model.CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField(null=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        end_at = None
        if self.end_at:
            end_at = f"'{self.end_at}'"
        return f"'id': {self.book.id}, " \
               f"'user': {repr(self.user)}, " \
               f"'book': {repr(self.book)}, " \
               f"'created_at': '{self.created_at}', " \
               f"'end_at': {end_at}, " \
               f"'plated_end_at': '{self.plated_end_at}'"

               # f"'book authors': '{self.book.authors}'"
               # f"'book description': '{self.book.description}', " \
               # f"'book count': '{self.book.count}', " \
               # f"'book authors': '{self.book.authors}'"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):
        """
        :return: dict contains order id, book id, user id, order created_at, order end_at, order plated_end_at
        :Example:
        | {
        |   'id': 8,
        |   'book': 8,
        |   'user': 8',
        |   'created_at': 1509393504,
        |   'end_at': 1509393504,
        |   'plated_end_at': 1509402866,
        | }
        """
        return_value = {
            'id': self.id,
            'book': self.book,
            'user': self.book,
            'created_at': int(f'{self.created_at.timestamp():.0f}'),
            'end_at': int(f'{self.end_at.timestamp():.0f}'),
            'plated_end_at': int(f'{self.plated_end_at.timestamp():.0f}'),
        }
        return return_value

    @staticmethod
    def create(user, book, plated_end_at):
        """
        :param user: the user who took the book
        :type user: CustomUser
        :param book: the book they took
        :type book: Book
        :param plated_end_at: planned return of data
        :type plated_end_at: int (timestamp)
        :return: a new order object which is also written into the DB
        """

        try:
            # if re.fullmatch(regex_for_mail, email):
            if user.id and book.count >= 10:
                new_order = Order(user=user,
                                  book=book,
                                  plated_end_at=plated_end_at)
                new_order.save()
                new_order.plated_end_at = plated_end_at
            else:

                raise DataError
        except (DataError, IntegrityError):
            new_order = None
        return new_order

    @staticmethod
    def get_by_id(order_id):
        """
        :param order_id:
        :type order_id: int
        :return:  the object of the order, according to the specified id or null in case of its absence
        """
        try:
            specific_order = Order.objects.get(id=order_id)
        except ObjectDoesNotExist:
            specific_order = None
        return specific_order

    def update(self, plated_end_at=None, end_at=None):
        """
        Updates order in the database with the specified parameters.\n
        :param plated_end_at: new plated_end_at
        :type plated_end_at: int (timestamp)
        :param end_at: new end_at
        :type plated_end_at: int (timestamp)
        :return: None
        """

        self.plated_end_at = plated_end_at if plated_end_at else self.plated_end_at
        self.end_at = end_at if end_at else self.end_at
        self.save()

        return None

    @staticmethod
    def get_all():
        """
        :return: all orders
        """
        return [order for order in Order.objects.all()]

    @staticmethod
    def get_not_returned_books():
        """
        :return:  all orders that do not have a return date (end_at)
        """
        return [order for order in Order.objects.all() if order.end_at is None]

    @staticmethod
    def delete_by_id(order_id):
        """
        :param order_id: an id of a user to be deleted
        :type order_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            specific_order = Order.objects.get(id=order_id)
            specific_order.delete()
        except ObjectDoesNotExist:
            specific_order = None
        return specific_order

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.modified = timezone.now()
    #     return super(Order, self).save(*args, **kwargs)
