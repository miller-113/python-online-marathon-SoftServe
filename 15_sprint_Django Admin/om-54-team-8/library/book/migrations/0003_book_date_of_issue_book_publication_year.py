# Generated by Django 4.1 on 2023-02-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_count_book_description_book_name_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_of_issue',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]