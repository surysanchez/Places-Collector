# Generated by Django 4.2 on 2023-04-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(verbose_name='review date'),
        ),
        migrations.AddField(
            model_name='place',
            name='attractions',
            field=models.ManyToManyField(to='main_app.attraction'),
        ),
    ]
