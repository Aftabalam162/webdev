# Generated by Django 4.2.2 on 2023-06-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_alter_bookissue_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='returnedDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
