# Generated by Django 4.1.6 on 2023-03-20 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blood', '0005_remove_bloodrequestmodel_is_donor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodrequestmodel',
            name='requested_donor_id',
        ),
    ]
