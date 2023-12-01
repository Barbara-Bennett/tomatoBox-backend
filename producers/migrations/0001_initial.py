# Generated by Django 4.1.1 on 2023-12-01 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('producerId', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=255)),
                ('box_premium', models.IntegerField(default=0)),
                ('box_common', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProducerTransaction',
            fields=[
                ('producerTransactionId', models.AutoField(primary_key=True, serialize=False)),
                ('producer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('transaction_type', models.CharField(choices=[('lend', 'Lend'), ('devolution', 'Devolution')], max_length=15)),
                ('box_type', models.CharField(choices=[('premium', 'Premium'), ('common', 'Common')], max_length=10)),
                ('box_qtt', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='producers.producer')),
            ],
        ),
    ]
