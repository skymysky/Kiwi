# Generated by Django 2.0.6 on 2018-06-29 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0018_remove_checksum_fields'),
    ]

    atomic = False

    operations = [
        migrations.AlterModelOptions(
            name='testcasestatus',
            options={
                        'verbose_name': 'Test case status',
                        'verbose_name_plural': 'Test case statuses'
                    },
        ),
        migrations.AlterModelTable(
            name='bug',
            table=None,
        ),
        migrations.AlterModelTable(
            name='bugsystem',
            table=None,
        ),
        migrations.AlterModelTable(
            name='category',
            table=None,
        ),
        migrations.AlterModelTable(
            name='contact',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testcase',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testcasecomponent',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testcaseplan',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testcasestatus',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testcasetag',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testcasetext',
            table=None,
        ),
    ]