# Generated by Django 5.0.6 on 2024-06-29 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0021_alter_borrow_history_borrower_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow_history',
            name='Date_Returned',
        ),
        migrations.RemoveField(
            model_name='borrow_history',
            name='Time_borrowed',
        ),
        migrations.RemoveField(
            model_name='borrow_history',
            name='Time_returned',
        ),
    ]
