# Generated by Django 5.0.6 on 2024-06-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0014_borrow_history_date_borrowed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_history',
            name='Time_returned',
            field=models.TimeField(null=True),
        ),
    ]