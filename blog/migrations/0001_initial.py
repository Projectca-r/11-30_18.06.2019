# Generated by Django 2.2.2 on 2019-06-18 08:05

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
            ],
        ),
        migrations.CreateModel(
            name='Category_a_laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('catalog', models.ManyToManyField(blank=True, related_name='a_laptop_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Category_Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('catalog', models.ManyToManyField(blank=True, related_name='phone_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Category_TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('catalog', models.ManyToManyField(blank=True, related_name='tv_catalog', to='blog.Catalog')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Product_TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('screen', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('size', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='catalog_tv', to='blog.Catalog')),
                ('category_tv', models.ManyToManyField(blank=True, related_name='tv', to='blog.Category_TV')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('camera', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('connect', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='catalog_phone', to='blog.Catalog')),
                ('category_phone', models.ManyToManyField(blank=True, related_name='phone', to='blog.Category_Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Product_a_laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to=blog.models.media)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('touch', models.CharField(blank=True, db_index=True, max_length=30)),
                ('weight', models.CharField(db_index=True, max_length=30)),
                ('memory', models.CharField(db_index=True, max_length=30)),
                ('onnect', models.CharField(db_index=True, max_length=30)),
                ('thickness', models.CharField(db_index=True, max_length=30)),
                ('ssd', models.CharField(db_index=True, max_length=30)),
                ('decimal', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('catalog', models.ManyToManyField(blank=True, related_name='catalog_a_laptop', to='blog.Catalog')),
                ('category_a_laptop', models.ManyToManyField(blank=True, related_name='a_laptop', to='blog.Category_a_laptop')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('product_a_laptop', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Product_a_laptop')),
                ('product_phone', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Product_Phone')),
                ('product_tv', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Product_TV')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=15)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='blog.OrderItem')),
            ],
        ),
    ]