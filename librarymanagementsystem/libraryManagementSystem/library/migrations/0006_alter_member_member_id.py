# Generated by Django 4.2.2 on 2023-06-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_member_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
