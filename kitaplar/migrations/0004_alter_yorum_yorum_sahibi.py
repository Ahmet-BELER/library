# Generated by Django 4.1.7 on 2023-03-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0003_alter_yorum_yorum_sahibi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='yorum_sahibi',
            field=models.CharField(max_length=255),
        ),
    ]