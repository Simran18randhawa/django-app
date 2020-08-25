# Generated by Django 2.1.15 on 2020-08-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20200821_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
    ]
