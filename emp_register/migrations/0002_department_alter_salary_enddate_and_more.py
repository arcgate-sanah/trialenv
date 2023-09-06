# Generated by Django 4.2.4 on 2023-09-06 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='salary',
            name='endDate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp_register.enddate'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='startDate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp_register.startdate'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_register.department'),
        ),
    ]
