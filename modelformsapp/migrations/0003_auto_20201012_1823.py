# Generated by Django 3.1.2 on 2020-10-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelformsapp', '0002_auto_20201012_1600'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='author',
            name='bookname',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3),
        ),
    ]
