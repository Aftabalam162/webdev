# Generated by Django 4.2.2 on 2023-06-17 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_librarian_groups_librarian_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookissue',
            name='transaction_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='library.transaction'),
            preserve_default=False,
        ),
    ]
