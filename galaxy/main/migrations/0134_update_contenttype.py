# Generated by Django 2.1.7 on 2019-03-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0133_collection_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='name',
            field=models.CharField(
                choices=[
                    ('apb', 'Ansible Playbook Bundle'),
                    ('role', 'Role'),
                    ('module', 'Module'),
                    ('module_utils', 'Module Utils'),
                    ('action', 'Action Plugin'),
                    ('become', 'Become Plugin'),
                    ('cache', 'Cache Plugin'),
                    ('callback', 'Callback Plugin'),
                    ('cliconf', 'CLI Conf Plugin'),
                    ('connection', 'Connection Plugin'),
                    ('doc_fragments', 'Doc Fragments Plugin'),
                    ('filter', 'Filter Plugin'),
                    ('httpapi', 'HTTP API Plugin'),
                    ('inventory', 'Inventory Plugin'),
                    ('lookup', 'Lookup Plugin'),
                    ('netconf', 'Netconf Plugin'),
                    ('shell', 'Shell Plugin'),
                    ('strategy', 'Strategy Plugin'),
                    ('terminal', 'Terminal Plugin'),
                    ('test', 'Test Plugin'),
                    ('vars', 'Vars Plugin')
                ],
                db_index=True,
                max_length=512,
                unique=True),
        ),
    ]
