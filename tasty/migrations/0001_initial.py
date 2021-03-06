# Generated by Django 3.0.6 on 2020-05-17 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('cooked_date', models.DateTimeField(verbose_name='date cooked')),
            ],
        ),
        migrations.CreateModel(
            name='Tasty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasty_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasty.Food')),
            ],
        ),
    ]
