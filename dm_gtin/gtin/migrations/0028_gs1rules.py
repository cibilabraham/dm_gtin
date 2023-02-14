# Generated by Django 3.0.4 on 2023-02-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtin', '0027_delete_gs1rules'),
    ]

    operations = [
        migrations.CreateModel(
            name='GS1Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FieldName', models.CharField(max_length=100)),
                ('Rules', models.TextField(null=True)),
                ('ValidationMessage', models.CharField(max_length=225)),
                ('Enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
