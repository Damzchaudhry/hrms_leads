# Generated by Django 2.0 on 2019-08-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('dept', models.CharField(choices=[('Web Development', 'Web Development'), ('Application Development', 'Application Development')], max_length=100)),
                ('job_location', models.CharField(max_length=100, verbose_name='job_location')),
                ('vacancy', models.CharField(max_length=10, verbose_name='vacancy')),
                ('exp', models.CharField(max_length=100, verbose_name='exp')),
                ('salary_from', models.CharField(max_length=100, verbose_name='salary_from')),
                ('salary_to', models.CharField(max_length=100, verbose_name='salary_to')),
                ('job_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], max_length=450, verbose_name='job_type')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=140, verbose_name='status')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='start_date')),
                ('end_date', models.DateField(default='2020-07-01', verbose_name='end_date')),
                ('desc', models.CharField(max_length=1500, verbose_name='desc')),
                ('skill', models.CharField(max_length=5000, verbose_name='skill')),
                ('email', models.CharField(max_length=55, verbose_name='email')),
                ('contact', models.CharField(max_length=15, verbose_name='contact')),
            ],
        ),
    ]