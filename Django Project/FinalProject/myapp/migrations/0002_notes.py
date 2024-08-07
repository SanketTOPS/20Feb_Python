# Generated by Django 5.0.6 on 2024-07-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('opt', models.CharField(max_length=50)),
                ('myfile', models.FileField(upload_to='Notes Files')),
                ('desc', models.TextField()),
            ],
        ),
    ]
