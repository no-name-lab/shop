# Generated by Django 5.1.1 on 2024-09-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze'), ('simple', 'Simple')], default='simple', max_length=10),
        ),
    ]
