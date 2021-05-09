

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0006_auto_20200219_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(verbose_name='Similarity')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar_items', to='movies.Movie')),
                ('other_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.AddConstraint(
            model_name='similarity',
            constraint=models.UniqueConstraint(fields=('movie', 'other_movie'), name='similarity'),
        ),
    ]
