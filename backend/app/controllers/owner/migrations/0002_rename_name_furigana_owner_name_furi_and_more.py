# Generated by Django 4.2.2 on 2023-06-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='name_furigana',
            new_name='name_furi',
        ),
        migrations.AlterField(
            model_name='ownermember',
            name='role',
            field=models.CharField(choices=[('owner', 'Owner'), ('admin', 'Admin'), ('member', 'Member')], default='member', max_length=50),
        ),
    ]
