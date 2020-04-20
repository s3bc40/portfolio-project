# Generated by Django 3.0.5 on 2020-04-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField(verbose_name='Date of birth')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='')),
                ('twitter', models.URLField(null=True, verbose_name='Twitter URL')),
                ('linkedin', models.URLField(null=True, verbose_name='Linkedin URL')),
                ('github', models.URLField(null=True, verbose_name='GitHub URL')),
                ('instagram', models.URLField(null=True, verbose_name='Instragram URL')),
                ('facebook', models.URLField(null=True, verbose_name='Facebook URL')),
            ],
        ),
    ]
