# Generated by Django 3.1.1 on 2022-06-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20200920_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='bookstore.Tag'),
        ),
    ]
