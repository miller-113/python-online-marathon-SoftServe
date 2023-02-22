from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    authors_ = serializers.StringRelatedField(many=True, source='authors')
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'count',
                  'publication_year', 'date_of_issue', 'authors_']
        # fields = '__all__'
