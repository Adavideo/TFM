# Generated by Django 3.0.3 on 2020-07-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics_identifier', '0003_cluster_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cluster',
            old_name='dataset',
            new_name='tree_name',
        ),
    ]
