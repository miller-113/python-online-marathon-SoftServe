from rest_framework import serializers
from .models import Author


class AuthorsSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="author-api:author")
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']

    def create(self, validated_data):

        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)
