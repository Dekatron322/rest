# Generated by Django 3.1.2 on 2020-10-15 08:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=60)),
                ('email', models.CharField(default='none', max_length=60)),
                ('phone', models.CharField(default='none', max_length=60)),
                ('message', models.CharField(default='none', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DessertB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DessertMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DrinkB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DrinkMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MainB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=50)),
                ('email', models.CharField(default='none', max_length=50)),
                ('phone', models.CharField(default='none', max_length=50)),
                ('number', models.IntegerField(default=1)),
                ('date', models.CharField(default='10/10/2020', max_length=50)),
                ('time', models.CharField(default='12:00pm', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=350)),
                ('description', models.CharField(max_length=350)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('company', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('footer', models.TextField(blank=True, max_length=50)),
                ('newsletter', models.CharField(blank=True, max_length=50)),
                ('smtppassword', models.CharField(blank=True, max_length=50)),
                ('smtpport', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, upload_to='images')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('aboutheader', models.TextField(blank=True, max_length=500)),
                ('aboutus', models.TextField(blank=True, max_length=500)),
                ('contact', models.TextField(blank=True, max_length=500)),
                ('references', models.TextField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('image', models.ImageField(upload_to='images')),
                ('imagetwo', models.ImageField(upload_to='images')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(default='none', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]