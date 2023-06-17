# Generated by Django 4.2.2 on 2023-06-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_member_books_issued_alter_member_fine_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissue',
            name='fine_charged',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]