
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0002_auto_20220111_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('emailid', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=300, null=True)),
                ('isread', models.CharField(max_length=10)),
                ('mdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
