# Generated by Django 3.2 on 2022-04-29 11:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gugols', '0004_auto_20220421_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='image',
            field=models.ImageField(null=True, upload_to='expert_images'),
        ),
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=11)),
                ('message', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gugols.category')),
            ],
            options={
                'verbose_name': 'Записываюший человек',
                'verbose_name_plural': 'Записываюший человеки',
            },
        ),
    ]