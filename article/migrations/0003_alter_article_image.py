# Generated by Django 5.0.6 on 2024-06-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images', verbose_name='Sekil'),
        ),
    ]
