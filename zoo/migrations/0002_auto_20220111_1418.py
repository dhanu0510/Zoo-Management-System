

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticforeigner',
            name='PostingDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ticindian',
            name='PostingDate',
            field=models.DateTimeField(null=True),
        ),
    ]
