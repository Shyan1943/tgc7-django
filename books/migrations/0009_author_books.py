# Generated by Django 2.2.14 on 2020-07-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
