# Generated by Django 5.0.2 on 2024-07-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEK', '0003_lekdocforms_lekplans_alter_lek_creation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LEKMeetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название документа')),
                ('title_ru', models.CharField(null=True, verbose_name='Название документа')),
                ('title_kk', models.CharField(null=True, verbose_name='Название документа')),
                ('title_en', models.CharField(null=True, verbose_name='Название документа')),
                ('document', models.FileField(blank=True, upload_to='LEK', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Заседание',
                'verbose_name_plural': 'Заседания ЛЭК',
            },
        ),
        migrations.CreateModel(
            name='LEKRegulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название документа')),
                ('title_ru', models.CharField(null=True, verbose_name='Название документа')),
                ('title_kk', models.CharField(null=True, verbose_name='Название документа')),
                ('title_en', models.CharField(null=True, verbose_name='Название документа')),
                ('document', models.FileField(blank=True, upload_to='LEK', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Положение',
                'verbose_name_plural': 'Положения ЛЭК',
            },
        ),
        migrations.AlterModelOptions(
            name='lek',
            options={'verbose_name': 'Информация', 'verbose_name_plural': 'Информация'},
        ),
        migrations.RemoveField(
            model_name='lek',
            name='meetings',
        ),
        migrations.RemoveField(
            model_name='lek',
            name='meetings_en',
        ),
        migrations.RemoveField(
            model_name='lek',
            name='meetings_kk',
        ),
        migrations.RemoveField(
            model_name='lek',
            name='meetings_ru',
        ),
        migrations.RemoveField(
            model_name='lek',
            name='regulation',
        ),
        migrations.AlterField(
            model_name='lek',
            name='contacts',
            field=models.TextField(blank=True, verbose_name='Контакты секретариата'),
        ),
        migrations.AlterField(
            model_name='lek',
            name='contacts_en',
            field=models.TextField(blank=True, null=True, verbose_name='Контакты секретариата'),
        ),
        migrations.AlterField(
            model_name='lek',
            name='contacts_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Контакты секретариата'),
        ),
        migrations.AlterField(
            model_name='lek',
            name='contacts_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Контакты секретариата'),
        ),
        migrations.AlterField(
            model_name='lek',
            name='standarts',
            field=models.TextField(blank=True, verbose_name='Стандартные операционные процедуры'),
        ),
        migrations.AlterField(
            model_name='lek',
            name='standarts_en',
            field=models.TextField(blank=True, null=True, verbose_name='Стандартные операционные процедуры'),
        ),
        migrations.AlterField(
            model_name='lek',
            name='standarts_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Стандартные операционные процедуры'),
        ),
        migrations.AlterField(
            model_name='lek',
            name='standarts_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Стандартные операционные процедуры'),
        ),
    ]