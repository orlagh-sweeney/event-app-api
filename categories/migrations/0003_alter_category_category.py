# Generated by Django 3.2.21 on 2023-09-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('sport', 'SPORT'), ('music', 'MUSIC'), ('culture', 'CULTURE'), ('books', 'BOOKS'), ('education', 'EDUCATION'), ('business', 'BUSINESS'), ('fitness', 'FITNESS'), ('food_drink', 'FOOD AND DRINK'), ('games', 'GAMES')], max_length=30),
        ),
    ]
