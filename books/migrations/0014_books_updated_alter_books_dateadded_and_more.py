# Generated by Django 4.0.6 on 2022-10-25 19:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_books_dateadded_alter_books_dateread'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='updated',
            field=models.DateTimeField(default=None, verbose_name=datetime.datetime(2022, 10, 25, 19, 46, 2, 99968, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='dateAdded',
            field=models.DateTimeField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='dateRead',
            field=models.DateTimeField(default=0, null=True),
        ),
    ]
