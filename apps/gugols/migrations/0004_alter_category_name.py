# Generated by Django 3.2 on 2022-06-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gugols', '0003_alter_signin_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Выберите услугу'),
        ),
    ]