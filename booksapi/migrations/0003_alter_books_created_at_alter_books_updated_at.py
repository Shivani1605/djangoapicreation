# Generated by Django 4.1 on 2022-08-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapi', '0002_alter_books_created_at_alter_books_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
