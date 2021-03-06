# Generated by Django 3.1 on 2021-07-01 00:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('list_image', stdimage.models.StdImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_code', models.CharField(blank=True, default='', max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
