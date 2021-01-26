# Generated by Django 3.1.4 on 2021-01-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]