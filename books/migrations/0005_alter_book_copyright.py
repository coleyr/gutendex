# Generated by Django 4.0.2 on 2022-02-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_copyright'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copyright',
            field=models.BooleanField(default=True),
        ),
    ]
