# Generated by Django 4.2.2 on 2023-06-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_alter_book_author_alter_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='num_of_copies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
