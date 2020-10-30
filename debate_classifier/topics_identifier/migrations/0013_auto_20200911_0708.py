# Generated by Django 3.0.3 on 2020-09-11 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics_identifier', '0012_auto_20200903_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cluster',
            name='reference_document',
            field=models.CharField(max_length=25000, null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='terms',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics_identifier.Tree'),
        ),
    ]