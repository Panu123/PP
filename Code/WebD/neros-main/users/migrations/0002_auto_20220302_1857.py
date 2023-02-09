# Generated by Django 3.2.12 on 2022-03-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
                ('users', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
