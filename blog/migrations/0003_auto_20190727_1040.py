# Generated by Django 2.2.3 on 2019-07-27 10:40

from django.db import migrations,models



class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='', max_length=501),
           
        ),
    ]
