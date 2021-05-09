

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True, verbose_name='TMDB ID')),
                ('imdb_id', models.CharField(max_length=16, unique=True, verbose_name='IMDB ID')),
                ('title', models.CharField(max_length=64, verbose_name='Movie title (original)')),
                ('title_kr', models.CharField(max_length=64, verbose_name='Movie title (Korean)')),
                ('release_date', models.DateField(null=True, verbose_name='Release date')),
                ('release_year', models.IntegerField(null=True, verbose_name='Release year')),
                ('runtime', models.IntegerField(null=True, verbose_name='Running time')),
                ('tagline', models.CharField(max_length=255, verbose_name='Tag line')),
                ('overview', models.TextField(verbose_name='Plot overview (EN)')),
                ('overview_kr', models.TextField(verbose_name='Plot overview (KR)')),
                ('poster', models.ImageField(null=True, upload_to='posters/', verbose_name='Movie poster')),
                ('alt_poster', models.TextField(verbose_name='Alt. poster URL')),
                ('imdb_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='IMDB avg. score')),
                ('tmdb_score', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='TMDB avg. score')),
                ('tmdb_popularity', models.FloatField(null=True, verbose_name='TMDB Popularity (daily)')),
                ('is_init_state', models.BooleanField(default=True, verbose_name='Initial state?')),
                ('tmdb_ok', models.BooleanField(default=False, verbose_name='Got all data from TMDB?')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last updated on')),
            ],
        ),
        migrations.CreateModel(
            name='MovieLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Language', verbose_name='Language')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_languages', to='movies.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Genre', verbose_name='Genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_genres', to='movies.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Person', verbose_name='Director')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_directors', to='movies.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Country', verbose_name='Country')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_countries', to='movies.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Company', verbose_name='Production company')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_companies', to='movies.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.Person', verbose_name='Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_actors', to='movies.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.AddConstraint(
            model_name='movielanguage',
            constraint=models.UniqueConstraint(fields=('movie', 'language'), name='Movie language'),
        ),
        migrations.AddConstraint(
            model_name='moviegenre',
            constraint=models.UniqueConstraint(fields=('movie', 'genre_id'), name='Movie genre'),
        ),
        migrations.AddConstraint(
            model_name='moviedirector',
            constraint=models.UniqueConstraint(fields=('movie', 'director'), name='Movie director'),
        ),
        migrations.AddConstraint(
            model_name='moviecountry',
            constraint=models.UniqueConstraint(fields=('movie', 'country'), name='Movie country'),
        ),
        migrations.AddConstraint(
            model_name='moviecompany',
            constraint=models.UniqueConstraint(fields=('movie', 'company'), name='Movie company'),
        ),
        migrations.AddConstraint(
            model_name='movieactor',
            constraint=models.UniqueConstraint(fields=('movie', 'actor'), name='Movie actor'),
        ),
    ]
