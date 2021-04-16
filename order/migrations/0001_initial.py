# Generated by Django 3.1.1 on 2020-09-05 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'New'), (20, 'Paid'), (30, 'Done')], default=10)),
                ('billing_name', models.CharField(max_length=100)),
                ('billing_contact', models.CharField(max_length=100)),
                ('billing_address1', models.CharField(max_length=100)),
                ('billing_address2', models.CharField(blank=True, max_length=100)),
                ('billing_city', models.CharField(max_length=100)),
                ('billing_zipcode', models.CharField(max_length=100)),
                ('billing_state', models.CharField(max_length=100)),
                ('billing_country', models.CharField(max_length=100)),
                ('shipping_name', models.CharField(max_length=100)),
                ('shipping_contact', models.CharField(max_length=100)),
                ('shipping_address1', models.CharField(max_length=100)),
                ('shipping_address2', models.CharField(blank=True, max_length=100)),
                ('shipping_city', models.CharField(max_length=100)),
                ('shipping_zipcode', models.CharField(max_length=100)),
                ('shipping_state', models.CharField(max_length=100)),
                ('shipping_country', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'New'), (20, 'Processing'), [30, 'Sent'], (40, 'Cancelled')], default=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
