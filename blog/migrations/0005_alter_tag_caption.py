# Generated by Django 5.0.6 on 2024-05-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='caption',
            field=models.CharField(max_length=50, null=True),
        ),
    ]