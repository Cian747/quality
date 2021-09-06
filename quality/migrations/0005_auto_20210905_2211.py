# Generated by Django 3.2.6 on 2021-09-05 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0004_rename_owner_images_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='location',
        ),
        migrations.AddField(
            model_name='images',
            name='location',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.DO_NOTHING, to='quality.location'),
            preserve_default=False,
        ),
    ]