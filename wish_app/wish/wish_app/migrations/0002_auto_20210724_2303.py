# Generated by Django 2.2 on 2021-07-24 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='granted_wishes',
        ),
        migrations.CreateModel(
            name='Granted_Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('granted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes_granted', to='wish_app.User')),
            ],
        ),
    ]
