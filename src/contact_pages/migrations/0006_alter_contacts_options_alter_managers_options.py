# Generated by Django 5.0.2 on 2024-05-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_pages', '0005_alter_contacts_options_alter_managers_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты НИИ'},
        ),
        migrations.AlterModelOptions(
            name='managers',
            options={'verbose_name': 'Руководитель', 'verbose_name_plural': 'Руководители'},
        ),
    ]