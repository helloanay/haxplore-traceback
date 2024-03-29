# Generated by Django 2.2.4 on 2019-08-24 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name_plural': 'Communities'},
        ),
        migrations.AddField(
            model_name='communityanswer',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='communityanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='community.CommunityQuestion'),
        ),
        migrations.AlterField(
            model_name='communityfarmer',
            name='farmer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community', to='core.Farmer'),
        ),
    ]
