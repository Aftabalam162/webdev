# Generated by Django 4.2.2 on 2023-06-13 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('isbn', models.BigIntegerField(primary_key=True, serialize=False)),
                ('num_of_copies', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('membership_status', models.CharField(max_length=10)),
                ('books_issued', models.CharField(max_length=255)),
                ('fine_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned_date', models.DateField()),
                ('comments', models.CharField(max_length=255)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member')),
            ],
        ),
    ]