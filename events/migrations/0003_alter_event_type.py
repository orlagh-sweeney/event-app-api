# Generated by Django 3.2.21 on 2023-09-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('sport', 'SPORT'), ('music', 'MUSIC'), ('culture', 'CULTURE'), ('books', 'BOOKS'), ('education', 'EDUCATION'), ('business', 'BUSINESS'), ('fitness', 'FITNESS'), ('food_drink', 'FOOD AND DRINK'), ('games', 'GAMES')], max_length=30),
        ),
    ]