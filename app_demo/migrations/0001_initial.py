# Generated by Django 2.2.5 on 2021-05-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayRechargeUserAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.CharField(max_length=50)),
                ('recharge_user_num', models.IntegerField()),
                ('recharge_amount_num', models.IntegerField()),
            ],
        ),
    ]
