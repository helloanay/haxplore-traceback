# Generated by Django 2.2.4 on 2019-08-24 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('district', models.CharField(max_length=32)),
                ('location_lat', models.FloatField(default=0)),
                ('location_lon', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_tags', models.TextField(default='')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('asked', models.DateTimeField(auto_now_add=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Community')),
                ('crop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Crop')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.Farmer')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityFarmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Community')),
                ('farmer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Farmer')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvotes', models.IntegerField(default=0)),
                ('is_correct', models.BooleanField(default=False)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.Farmer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.CommunityQuestion')),
            ],
        ),
    ]
