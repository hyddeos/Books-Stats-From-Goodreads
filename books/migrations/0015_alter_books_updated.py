# Generated by Django 4.0.6 on 2022-10-25 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_books_updated_alter_books_dateadded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='updated',
            field=models.DateTimeField(default=None, verbose_name=datetime.datetime(2022, 10, 25, 20, 3, 58, 275042)),
        ),
    ]
