# Generated by Django 3.2.7 on 2021-09-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
