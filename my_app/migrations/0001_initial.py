# Generated by Django 3.2.21 on 2024-02-11 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agriculture_office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('usertype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifications', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subsidy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('From', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.login')),
            ],
        ),
        migrations.CreateModel(
            name='success_story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('AGRICULTURE_OFFICE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.agriculture_office')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('AGRICULTURE_OFFICE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.agriculture_office')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('payment_status', models.CharField(max_length=100)),
                ('AGRICULTURE_OFFICE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.agriculture_office')),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='order_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('ORDERS', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.orders')),
                ('STOCK', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.stock')),
            ],
        ),
        migrations.CreateModel(
            name='notification_office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('AGRICULTURE_OFFICE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.agriculture_office')),
            ],
        ),
        migrations.CreateModel(
            name='fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('AGRICULTURE_OFFICE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.agriculture_office')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('reply_date', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('AGRICULTURE_OFFICE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.agriculture_office')),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('STOCK', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.stock')),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='agriculture_office',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.login'),
        ),
    ]