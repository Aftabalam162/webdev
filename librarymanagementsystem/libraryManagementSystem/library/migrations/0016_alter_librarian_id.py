# Generated by Django 4.2.2 on 2023-06-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_librarian_id_librarian_is_active_librarian_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
