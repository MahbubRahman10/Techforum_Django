# Generated by Django 2.2.2 on 2019-07-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionvisitor',
            name='visitor_ip',
            field=models.CharField(max_length=100),
        ),
    ]
