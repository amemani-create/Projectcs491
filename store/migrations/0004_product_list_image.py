# Generated by Django 3.1 on 2021-06-30 21:15

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210630_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='list_image',
            field=stdimage.models.StdImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]