# Generated by Django 3.2.5 on 2021-07-29 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=30)),
                ('comment', models.TextField(blank=True, max_length=1500, null=True)),
                ('task', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='NEW', on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.source')),
                ('user', models.ForeignKey(default='misen', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
