# Generated by Django 3.1.2 on 2021-10-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='img',
            field=models.ImageField(default='test', upload_to='shop/pattern/', verbose_name='画像'),
            preserve_default=False,
        ),
    ]