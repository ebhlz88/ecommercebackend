# Generated by Django 3.2 on 2021-06-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('productdisc', models.CharField(max_length=50)),
                ('product_photo', models.ImageField(upload_to='productimage')),
            ],
        ),
    ]