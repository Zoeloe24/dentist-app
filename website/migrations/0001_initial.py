# Generated by Django 3.0.2 on 2020-11-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='website/')),
                ('title', models.CharField(max_length=155)),
                ('content', models.TextField()),
            ],
        ),
    ]
