# Generated by Django 4.2.3 on 2023-07-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=50)),
                ('std_id', models.IntegerField()),
                ('std_course', models.CharField(max_length=50)),
                ('std_Phone_no', models.CharField(max_length=50)),
                ('std_class', models.CharField(max_length=10)),
            ],
        ),
    ]
