# Generated by Django 5.0 on 2023-12-31 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_excerpt"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
