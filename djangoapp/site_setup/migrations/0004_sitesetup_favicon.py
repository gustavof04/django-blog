# Generated by Django 4.2.7 on 2023-11-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_alter_sitesetup_options_menulink_site_setup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m'),
        ),
    ]
