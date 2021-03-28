# Generated by Django 3.1.7 on 2021-03-09 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(default='https://restolife.kz/upload/information_system_6/2/2/1/item_22198/information_items_property_25471.jpg', max_length=255)),
                ('address', models.CharField(default='Tole bi, 170', max_length=100)),
                ('contact', models.CharField(default='+7 (707) 777 77 77', max_length=100)),
                ('avg_cost', models.IntegerField(default=4500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=3000)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='api.restaurant')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
            },
        ),
    ]