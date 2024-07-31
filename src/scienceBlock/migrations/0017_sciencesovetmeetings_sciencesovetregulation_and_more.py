# Generated by Django 5.0.2 on 2024-07-31 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scienceBlock', '0016_remove_sciencesovetplans_document_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScienceSovetMeetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название документа')),
                ('title_ru', models.CharField(null=True, verbose_name='Название документа')),
                ('title_kk', models.CharField(null=True, verbose_name='Название документа')),
                ('title_en', models.CharField(null=True, verbose_name='Название документа')),
                ('document', models.FileField(blank=True, upload_to='science', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Заседание',
                'verbose_name_plural': 'Заседания НТС',
            },
        ),
        migrations.CreateModel(
            name='ScienceSovetRegulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название документа')),
                ('title_ru', models.CharField(null=True, verbose_name='Название документа')),
                ('title_kk', models.CharField(null=True, verbose_name='Название документа')),
                ('title_en', models.CharField(null=True, verbose_name='Название документа')),
                ('document', models.FileField(blank=True, upload_to='science', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Положение',
                'verbose_name_plural': 'Положения НТС',
            },
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='meetings',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='meetings_en',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='meetings_kk',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='meetings_ru',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='regulation',
        ),
        migrations.AddField(
            model_name='sciencesovet',
            name='creation_title',
            field=models.CharField(default=13, verbose_name='Название приказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sciencesovet',
            name='creation_title_en',
            field=models.CharField(null=True, verbose_name='Название приказа'),
        ),
        migrations.AddField(
            model_name='sciencesovet',
            name='creation_title_kk',
            field=models.CharField(null=True, verbose_name='Название приказа'),
        ),
        migrations.AddField(
            model_name='sciencesovet',
            name='creation_title_ru',
            field=models.CharField(null=True, verbose_name='Название приказа'),
        ),
    ]