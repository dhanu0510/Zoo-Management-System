

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AnimalName', models.CharField(max_length=200, null=True)),
                ('CageNumber', models.CharField(max_length=15, null=True)),
                ('FeedNumber', models.CharField(max_length=150, null=True)),
                ('Breed', models.CharField(max_length=200, null=True)),
                ('AnimalImage', models.FileField(max_length=200, null=True, upload_to='')),
                ('Description', models.CharField(max_length=300, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticforeigner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketID', models.CharField(max_length=100, null=True)),
                ('NoAdult', models.CharField(max_length=50, null=True)),
                ('NoChildren', models.CharField(max_length=50, null=True)),
                ('AdultUnitprice', models.CharField(max_length=100, null=True)),
                ('ChildUnitprice', models.CharField(max_length=100, null=True)),
                ('PostingDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticindian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketID', models.CharField(max_length=100, null=True)),
                ('NoAdult', models.CharField(max_length=50, null=True)),
                ('NoChildren', models.CharField(max_length=50, null=True)),
                ('AdultUnitprice', models.CharField(max_length=100, null=True)),
                ('ChildUnitprice', models.CharField(max_length=100, null=True)),
                ('PostingDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickettype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketType', models.CharField(max_length=200, null=True)),
                ('Price', models.CharField(max_length=150, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
