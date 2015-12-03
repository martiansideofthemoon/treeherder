# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_auto_20151130_1503'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='failureline',
            index_together=set([('job_guid', 'repository')]),
        ),
    ]
