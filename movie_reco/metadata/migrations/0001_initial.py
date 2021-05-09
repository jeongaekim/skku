from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='ISO-3166-1 alpha-2')),
                ('name', models.CharField(max_length=64, verbose_name='Country name')),
                ('name_kr', models.CharField(max_length=64, verbose_name='Country name (KR)')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='Genre name')),
                ('name_kr', models.CharField(max_length=32, verbose_name='Genre name (KR)')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='ISO-639-1 alpha-2')),
                ('name', models.CharField(max_length=64, verbose_name='Language name')),
                ('name_kr', models.CharField(max_length=64, verbose_name='Language name (KR)')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=16, unique=True, verbose_name='IMDB ID')),
                ('name', models.CharField(max_length=128, verbose_name="Person's name")),
            ],
        ),
    ]
