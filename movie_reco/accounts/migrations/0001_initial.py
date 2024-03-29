

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='User email')),
                ('password', models.CharField(max_length=128, verbose_name='User password')),
                ('type', models.IntegerField(choices=[(0, 'admin'), (1, 'user'), (2, 'bot')], verbose_name='User type')),
            ],
        ),
    ]
