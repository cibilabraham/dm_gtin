# Generated by Django 3.0.4 on 2023-02-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gtin', '0012_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtin', models.CharField(max_length=50)),
                ('BrandName', models.CharField(max_length=50)),
                ('BrandOwnerName', models.CharField(max_length=50, null=True)),
                ('SubBrandName', models.CharField(max_length=50, null=True)),
                ('Contact', models.CharField(max_length=50, null=True)),
                ('ContactTypeCode', models.CharField(max_length=50, null=True)),
                ('ContactMethodCode', models.CharField(max_length=50, null=True)),
                ('ContactAddress', models.TextField(null=True)),
                ('ContactDetails', models.TextField(null=True)),
                ('ShortProductName', models.CharField(max_length=50)),
                ('ProductMarketingMessage', models.TextField(null=True)),
                ('SearchKeyWordsforProduct', models.TextField(null=True)),
                ('ProductTypeDescription', models.TextField()),
                ('DataProviderName', models.CharField(max_length=50, null=True)),
                ('ManufacturerName', models.CharField(max_length=50, null=True)),
                ('GPCCode', models.CharField(max_length=50, null=True)),
                ('MarketAvailabilityDate', models.DateField(null=True)),
                ('Length', models.IntegerField(default=0)),
                ('LengthUnit', models.CharField(max_length=10)),
                ('Height', models.IntegerField(default=0)),
                ('HeightUnit', models.CharField(max_length=10)),
                ('Width', models.IntegerField(default=0)),
                ('WidthUnit', models.CharField(max_length=10)),
                ('GrossWeight', models.IntegerField(default=0)),
                ('GrossWeightUnit', models.CharField(max_length=10)),
                ('AllergenContainmentCode', models.CharField(max_length=50, null=True)),
                ('AllergenTypeCode', models.CharField(max_length=50, null=True)),
                ('AllergenStatement', models.CharField(max_length=50, null=True)),
                ('IngredientStatement', models.TextField(null=True)),
                ('FeedTypeCertification', models.CharField(max_length=50, null=True)),
                ('AllergenDeclarationsIndicator', models.BooleanField(default=False)),
                ('svrStatus', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
