# Generated by Django 2.0.6 on 2018-08-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='')),
                ('Class', models.CharField(choices=[('ONE', 'ONE'), ('TWO', 'TWO'), ('THREE', 'THREE'), ('FOUR', 'FOUR'), ('FIVE', 'FIVE'), ('SIX', 'SIX'), ('SEVEN', 'SEVEN'), ('EIGHT', 'EIGHT')], default='EIGHT', help_text='Enter the current class you are in', max_length=255)),
                ('subject', models.CharField(blank=True, default='', help_text='Enter the subject of the book', max_length=140)),
            ],
            options={
                'db_table': 'EResources',
            },
        ),
        migrations.AlterModelTable(
            name='pdfresources',
            table='PdfResources',
        ),
    ]
