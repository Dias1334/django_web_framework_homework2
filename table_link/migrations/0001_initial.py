# Generated by Django 4.2.1 on 2023-07-04 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('Date_of_issue', models.DateField()),
                ('janre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='table_link.category')),
            ],
        ),
    ]