# Generated by Django 2.2 on 2019-04-28 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModelServiceItemMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_model', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('service_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testapp.ServiceItem')),
            ],
        ),
    ]