# Generated by Django 4.0.4 on 2022-05-22 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbapi', '0003_alter_comments_id_alter_district_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soil',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dbapi.district'),
        ),
        migrations.AddField(
            model_name='weather',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dbapi.district'),
        ),
        migrations.CreateModel(
            name='AnalyzedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('sowing', models.BooleanField()),
                ('harvesting', models.BooleanField()),
                ('district', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dbapi.district')),
            ],
        ),
    ]
